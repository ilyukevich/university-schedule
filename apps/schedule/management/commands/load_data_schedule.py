from django.core.management.base import BaseCommand, CommandError

from apps.accounts.models import Account
from apps.schedule.models import Lessons, Schedule
from apps.schedule.constants import DAY, TIME
from apps.university.models import Faculties, Departaments, StudyGroups, Auditories, Disciplines


class Command(BaseCommand):
    """Base command for load data for app Schedule into database"""

    help = '>>> load data for app Schedule into database (Lessons, Schedule)'
    print(help)

    def handle(self, *args, **kwargs):
        """Base command for load data into database (loading data for the Schedule application)"""

        faculty_name = 'Faculty of Computer Design'
        departament_name = 'Department of Information and Computer Systems Design'
        studygroup_name = '812501'
        auditory_names = ['1', '2', '3', '4', '5']
        discipline_names = ['Design', 'Management', 'Electronics', 'Networks', 'Infocommunications', 'Economics']
        days = tuple(DAY.keys())
        times = tuple(TIME.keys())

        # Lessons
        faculty = Faculties.objects.get(name=faculty_name)
        departament = Departaments.objects.get(name=departament_name)
        studygroup = StudyGroups.objects.get(name=studygroup_name)

        auditories_1 = Auditories.objects.get(name=auditory_names[0])
        auditories_2 = Auditories.objects.get(name=auditory_names[1])
        auditories_3 = Auditories.objects.get(name=auditory_names[2])
        auditories_4 = Auditories.objects.get(name=auditory_names[3])
        auditories_5 = Auditories.objects.get(name=auditory_names[4])

        disciplines_1 = Disciplines.objects.get(name=discipline_names[0])
        disciplines_2 = Disciplines.objects.get(name=discipline_names[1])
        disciplines_3 = Disciplines.objects.get(name=discipline_names[2])
        disciplines_4 = Disciplines.objects.get(name=discipline_names[3])
        disciplines_5 = Disciplines.objects.get(name=discipline_names[4])

        lesson_1 = Lessons.objects.create(lesson_name=disciplines_1, day=days[0], time=times[0], auditory=auditories_1)
        lesson_2 = Lessons.objects.create(lesson_name=disciplines_2, day=days[0], time=times[1], auditory=auditories_2)
        lesson_3 = Lessons.objects.create(lesson_name=disciplines_3, day=days[0], time=times[2], auditory=auditories_3)
        lesson_4 = Lessons.objects.create(lesson_name=disciplines_4, day=days[0], time=times[3], auditory=auditories_4)
        lesson_5 = Lessons.objects.create(lesson_name=disciplines_5, day=days[0], time=times[4], auditory=auditories_5)

        lesson_1.save()
        lesson_2.save()
        lesson_3.save()
        lesson_4.save()
        lesson_5.save()

        print('Create Lessons... OK')

        # Schedule
        student = Account.objects.get(username='admin')
        schedule = Schedule.objects.create(
            schedule_name='Schedule_1',
            student=student,
            faculty=faculty,
            departament=departament,
            studygroups=studygroup,
            day=days[0],
            available=True,
        )

        schedule.save()

        schedule.lessons.add(lesson_1)
        schedule.lessons.add(lesson_2)
        schedule.lessons.add(lesson_3)
        schedule.lessons.add(lesson_4)
        schedule.lessons.add(lesson_5)

        print('Create Schedule... OK')

        print('>>> Creation completed!')
