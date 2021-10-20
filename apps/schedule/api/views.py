from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..models import Lessons, Schedule
from .serializers import LessonsSerializers, ScheduleSerializers


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
