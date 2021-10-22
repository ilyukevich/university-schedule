from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema

from apps.accounts.models import Account
from apps.schedule.tasks import sent_schedule
from ..models import Lessons, Schedule
from .serializers import LessonsSerializers, ScheduleSerializers, ScheduleRequestSerializer


class LessonsViewSet(viewsets.ModelViewSet):
    """API endpoint Lessons"""

    queryset = Lessons.objects.all().order_by('-lesson_name')
    serializer_class = LessonsSerializers
    permission_classes = [IsAuthenticated]


class ScheduleViewSet(viewsets.ModelViewSet):
    """API endpoint Schedule"""

    queryset = Schedule.objects.all().order_by('-schedule_name')
    serializer_class = ScheduleSerializers
    permission_classes = [IsAuthenticated]


class ScheduleRequestAPIView(APIView):
    """API schedule request"""

    permission_classes = [AllowAny]
    serializer_class = ScheduleRequestSerializer

    @swagger_auto_schema(
        request_body=ScheduleRequestSerializer,
        responses={
            200: 'OK',
            400: 'Bad Request',
            403: 'Forbidden',
            404: 'Not Found'
        },
    )
    def post(self, request):
        """Request schedule for a student"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            day = serializer.validated_data['day']

            try:
                user_for_request = Account.objects.get(email__exact=email)

            except Exception as e:
                if str(e) == 'User matching query does not exist.':
                    return Response(status=status.HTTP_404_NOT_FOUND,
                                    data={"error": "Error, no user with this email!"})
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"error": str(e)})

            try:
                Schedule.objects.get(day=day)

            except Exception as e:
                if str(e) == 'Schedule matching query does not exist.':
                    return Response(status=status.HTTP_404_NOT_FOUND,
                                    data={"error": "Error, Schedule not found on this day!"})
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"error": str(e)})

            if Account.objects.get(email__exact=email):
                id_for_request = user_for_request.id
                username_for_request = user_for_request.id

                count_lessons = Schedule.objects.get(day=day, student=id_for_request).lessons.count()
                student_lessons = Schedule.objects.get(day=day, student=id_for_request).lessons.all()
                lessons = student_lessons.values()

                # # task. Sent email for user with his schedule
                # sent_schedule.delay(username_for_request, id_for_request, email, count_lessons, lessons, day)

                return Response(status=status.HTTP_200_OK,
                                data={
                                    "Day": day,
                                    "student": username_for_request,
                                    "id": id_for_request,
                                    "email": email,
                                    "count_lessons": {count_lessons},
                                    "lessons": lessons
                                }
                                )

            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": "No user with this email!"})

        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={"error": "Please enter a valid email address!"})
