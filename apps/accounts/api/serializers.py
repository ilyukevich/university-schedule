from rest_framework import serializers
from ..models import Account, UserProfile


class RegistrationSerializer(serializers.ModelSerializer):
    """RegistrationSerializer to create a new user with required fields role and email"""

    password = serializers.CharField(max_length=128, min_length=8, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = Account
        fields = ('username', 'password', 'email', 'role')


class LoginSerializer(serializers.Serializer):
    """LoginSerializer to login with field validation"""

    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True, style={'input_type': 'password'})


class LogoutSerializer(serializers.Serializer):
    """LogoutSerializer to logout"""


class ResetPasswordSerializer(serializers.Serializer):
    """ResetPasswordSerializer to reset password for user"""

    email = serializers.EmailField()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """UserList API"""

    class Meta:
        model = Account
        fields = ['id', 'email', 'username', 'first_name', 'last_name',
                  'role', 'is_active', 'is_staff', 'last_login', 'url']
        extra_kwargs = {
            'url': {
                'view_name': 'api:user-detail'
            },
        }


class UserProfileSerializer(serializers.ModelSerializer):
    """UserProfiles API"""

    class Meta:
        fields = '__all__'
        model = UserProfile
