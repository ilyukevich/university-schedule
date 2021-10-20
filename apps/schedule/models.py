from django.db import models
from apps.accounts.models import Account
from apps.university.models import Faculties, Departaments, StudyGroups, Auditories, Disciplines
from apps.schedule.constants import DAY, TIME


class Lessons(models.Model):
    """***"""

    DAY_ = tuple(DAY.items())
    TIME_ = tuple(TIME.items())

    lesson_name = models.ForeignKey(Disciplines, related_name='lesson_name', on_delete=models.CASCADE)
    day = models.CharField(max_length=30, choices=DAY_)
    time = models.CharField(max_length=30, choices=TIME_)
    auditory = models.ForeignKey(Auditories, related_name='auditories', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('lesson_name',)

    def __str__(self):
        return str(self.lesson_name)


class Schedule(models.Model):
    """***"""

    DAY_ = tuple(DAY.items())

    schedule_name = models.CharField(max_length=200, db_index=True)
    student = models.ForeignKey(Account, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculties, related_name='faculty', on_delete=models.CASCADE)
    departament = models.ForeignKey(Departaments, related_name='departament', on_delete=models.CASCADE)
    studygroups = models.ForeignKey(StudyGroups, related_name='studygroup', on_delete=models.CASCADE)
    day = models.CharField(max_length=30, choices=DAY_)
    lessons = models.ManyToManyField(Lessons, related_name='lessons',)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('schedule_name',)

    def __str__(self):
        return self.schedule_name
