from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..models import Faculties, Departaments, StudyGroups, Auditories, Disciplines
from .serializers import (FacultiesSerializers, DepartamentsSerializers, StudyGroupsSerializers,
                          AuditoriesSerializers, DisciplinesSerializers)


class FacultiesViewSet(viewsets.ModelViewSet):
    """API endpoint Faculties"""

    queryset = Faculties.objects.all().order_by('-name')
    serializer_class = FacultiesSerializers
    permission_classes = [IsAuthenticated]


class DepartamentsViewSet(viewsets.ModelViewSet):
    """API endpoint Departaments"""

    queryset = Departaments.objects.all().order_by('-name')
    serializer_class = DepartamentsSerializers
    permission_classes = [IsAuthenticated]


class StudyGroupsViewSet(viewsets.ModelViewSet):
    """API endpoint StudyGroups"""

    queryset = StudyGroups.objects.all().order_by('-name')
    serializer_class = StudyGroupsSerializers
    permission_classes = [IsAuthenticated]


class AuditoriesViewSet(viewsets.ModelViewSet):
    """API endpoint Auditories"""

    queryset = Auditories.objects.all().order_by('-name')
    serializer_class = AuditoriesSerializers
    permission_classes = [IsAuthenticated]


class DisciplinesViewSet(viewsets.ModelViewSet):
    """API endpoint Disciplines"""

    queryset = Disciplines.objects.all().order_by('-name')
    serializer_class = DisciplinesSerializers
    permission_classes = [IsAuthenticated]
