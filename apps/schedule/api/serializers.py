from rest_framework import serializers
from ..models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """RegistrationSerializer to create a new user with required fields role and email"""

    password = serializers.CharField(max_length=128, min_length=8, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'role')


class LoginSerializer(serializers.Serializer):
    """LoginSerializer to login with field validation"""

    username = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True, style={'input_type': 'password'})


class LogoutSerializer(serializers.Serializer):
    """LogoutSerializer to logout"""


class ResetPasswordSerializer(serializers.Serializer):
    """ResetPasswordSerializer to reset password for user"""

    email = serializers.EmailField()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """UserList"""

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name',
                  'role', 'is_active', 'is_staff', 'last_login', 'url']
        extra_kwargs = {
            'url': {
                'view_name': 'api:user-detail'
            },
        }
