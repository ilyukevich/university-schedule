from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from drf_yasg.utils import swagger_auto_schema
from .serializers import (UserSerializer, LoginSerializer, RegistrationSerializer,
                          LogoutSerializer, ResetPasswordSerializer)
from ..models import User
from apps.accountapp.tasks import user_created
import environ
import jwt
import random


env = environ.Env()
env.read_env(".env")


class RegistrationAPIView(APIView):
    """Create a new user"""

    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    @swagger_auto_schema(
        request_body=RegistrationSerializer,
        responses={
            201: 'Created',
            400: 'Bad Request',
            403: 'Forbidden',
        },
    )
    def post(self, request):
        """Create a new user with required fields role and email"""

        serializer = self.serializer_class(data=request.data)

        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        role = request.data['role']

        # field validation
        if not username:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error": "Username field is required"})
        if not password:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error": "Password field is required"})
        if len(password) < 8:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error": "Password length at least 8 characters"})
        if not email:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error": "Email field is required"})

        if User.objects.filter(username=username).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error": "Username exists"})
        if User.objects.filter(email=email).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error": "Email exists"})

        if serializer.is_valid(raise_exception=False):

            # getting groups
            group_administrators = Group.objects.get(name='Administrators')
            group_users = Group.objects.get(name='Users')
            serializer.save()

            # getting the current user
            user = User.objects.get(username=username)

            # obtaining rights for a user depending on the selected role
            if request.data['role'] == 'Administrator':
                user.groups.add(group_administrators)
                # is_staff for 'Administrators' default
                user.is_staff = True
                user.save()
            elif request.data['role'] == 'User':
                user.groups.add(group_users)

            # task. Sent email for user after success registration
            user_created.delay(username)

            return Response(status=status.HTTP_201_CREATED,
                            data={
                                "username": username,
                                "email": email,
                                "role": role,
                                  }
                            )
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=serializer.errors)


class LoginAPIView(APIView):
    """Login for user"""

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: 'OK',
            400: 'Bad Request',
            403: 'Forbidden',
            404: 'Not Found'
        },
    )
    def post(self, request):
        """Login for user. Check if the user exists, if the required fields are filled"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=False):

            username = request.data['username']
            password = request.data['password']

            user = authenticate(request, username=username, password=password)

            if not user:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data={"Error": "Check your username or password"})
            # login for user
            login(request, user)

            # get data for user
            data_ = User.objects.get(username=username)
            username = data_.username
            email = data_.email
            role = data_.role

            # encrypt the 'username', 'email', 'role' field
            secret = env.str("JWT_SECRET")
            algorithm = 'HS256'
            payload = {'username': username, 'email': email, 'role': role}
            encoded_fields = jwt.encode(payload, secret, algorithm=algorithm)
            #decoded_fields = jwt.decode(encoded_fields, secret, algorithms=['HS256'])

            return Response(status=status.HTTP_200_OK,
                            data={'OK': encoded_fields})
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={"Error": "Username and password fields is required"})


class LogoutAPIView(APIView):
    """Logout for user"""

    permission_classes = [AllowAny]
    serializer_class = LogoutSerializer

    @swagger_auto_schema(
        responses={
            200: 'OK',
        },
    )
    def post(self, request):
        """Logged out for user"""
        logout(request)
        return Response(status=status.HTTP_200_OK, data={"OK": "You are logged out!"})


class ResetPasswordAPIView(APIView):
    """API reset user password"""

    permission_classes = [AllowAny]
    serializer_class = ResetPasswordSerializer

    @swagger_auto_schema(
        request_body=ResetPasswordSerializer,
        responses={
            200: 'OK',
            400: 'Bad Request',
            403: 'Forbidden',
            404: 'Not Found'
        },
    )
    def post(self, request):
        """Reset password for a user via email"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            # symbols from generate new password
            symbols = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            new_password = ''
            length_pass = 8
            for i in range(int(length_pass)):
                new_password += random.choice(symbols)

            subject_ = 'New password for the service ImgService'
            from_ = 'img-service@img-service.com'
            message_ = f'Your new password: {new_password}'

            try:
                user_for_reset = User.objects.get(email__exact=email)
            except Exception as e:
                if str(e) == 'User matching query does not exist.':
                    return Response(status=status.HTTP_404_NOT_FOUND,
                                    data={"error": "Error, no user with this email!"})
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"error": str(e)})

            if User.objects.get(email__exact=email) or User.objects.get(email_2__exact=email):
                user_for_reset.set_password(new_password)
                user_for_reset.save()
                send_mail(subject_, message_, from_, [email],)
                return Response(status=status.HTTP_200_OK,
                                data={"OK": "A new password has been sent to your email!"})

            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": "No user with this email!"})

        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={"error": "Please enter a valid email address!"})


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
