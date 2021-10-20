from rest_framework import serializers
from ..models import Lessons, Schedule


class LessonsSerializers(serializers.ModelSerializer):
    """Lessons API"""

    class Meta:
        fields = '__all__'
        model = Lessons


class ScheduleSerializers(serializers.ModelSerializer):
    """Schedule API"""

    class Meta:
        fields = '__all__'
        model = Schedule
