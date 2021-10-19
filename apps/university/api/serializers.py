from rest_framework import serializers
from ..models import Faculties, Departaments, StudyGroups, Auditories, Disciplines


class FacultiesSerializers(serializers.ModelSerializer):
    """Faculties API"""

    class Meta:
        fields = '__all__'
        model = Faculties


class DepartamentsSerializers(serializers.ModelSerializer):
    """Departaments API"""

    class Meta:
        fields = '__all__'
        model = Departaments


class StudyGroupsSerializers(serializers.ModelSerializer):
    """StudyGroups API"""

    class Meta:
        fields = '__all__'
        model = StudyGroups


class AuditoriesSerializers(serializers.ModelSerializer):
    """Auditories API"""

    class Meta:
        fields = '__all__'
        model = Auditories


class DisciplinesSerializers(serializers.ModelSerializer):
    """Disciplines API"""

    class Meta:
        fields = '__all__'
        model = Disciplines
