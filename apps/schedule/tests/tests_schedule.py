from django.test import TestCase
from django.core.cache import cache

from apps.accounts.models import Account
from apps.schedule.models import Lessons, Schedule
from apps.university.models import Faculties, Departaments, StudyGroups, Auditories, Disciplines


class LessonsTest(TestCase):
    """Common tests to validate the Lessons model"""

    def setUp(self):
        """Fixtures"""
        self.day = 'Monday'
        self.time = '14:00-16:00'
        self.name_schedule = 'new_name_schedule'
        self.name_faculty = 'new_name_faculty'
        self.slug_faculty = 'new-slug-faculty'
        self.name_departament = 'new_name_departament'
        self.slug_departament = 'new-slug-departament'
        self.name_studygroup = 'new_name_studygroup'
        self.slug_studygroup = 'new-slug-studygroup'
        self.name_auditory = 'new_name_auditory'
        self.slug_auditory = 'new-slug-auditory'
        self.name_discipline = 'new_name_discipline'
        self.slug_discipline = 'new-slug-discipline'

        self.student = Account.objects.create(
            username='student',
            password='student',
            email='student@university-schedule.com',
            role='Student',
            is_active=True
        )
        self.new_faculty = Faculties.objects.create(name=self.name_faculty, slug=self.slug_faculty, )
        self.new_departament = Departaments.objects.create(
            faculty=self.new_faculty,
            name=self.name_departament,
            slug=self.slug_departament,
        )
        self.new_studygroup = StudyGroups.objects.create(
            departament=self.new_departament,
            name=self.name_studygroup,
            slug=self.slug_studygroup,
        )
        self.new_discipline = Disciplines.objects.create(name=self.name_discipline, slug=self.slug_discipline, )
        self.new_auditory = Auditories.objects.create(name=self.name_auditory, slug=self.slug_auditory, )
        self.new_lesson = Lessons.objects.create(
            lesson_name=self.new_discipline,
            day=self.day,
            time=self.time,
            auditory=self.new_auditory,
        )
        # clear cache before running tests
        cache.clear()

    def test_model_lessons(self):
        """test to validate the Lessons model"""

        # request initial number of objects Lessons
        total_count_obj = Lessons.objects.all().count()

        # checking the number of objects Lessons
        self.assertEqual(1, total_count_obj)

        # request fields of Lessons
        self.assertEqual(self.new_lesson.lesson_name, self.new_discipline)
        self.assertEqual(self.new_lesson.day, self.day)
        self.assertEqual(self.new_lesson.time, self.time)
        self.assertEqual(self.new_lesson.auditory, self.new_auditory)

        # request for the number of Lessons objects after creating a new one and check
        now_total_count_obj = Lessons.objects.all().count()
        now_total_count_obj2 = Lessons.objects.filter(lesson_name=self.new_discipline).filter(day=self.day).count()
        self.assertEqual(now_total_count_obj, total_count_obj)
        self.assertEqual(now_total_count_obj2, total_count_obj)

        # request from database and check new Lessons
        get_lesson = Lessons.objects.get(lesson_name=self.new_discipline, day=self.day,)
        self.assertEqual(get_lesson.lesson_name, self.new_discipline)
        self.assertEqual(get_lesson.day, self.day)


class ScheduleTest(LessonsTest):
    """Common tests to validate the Schedule model"""

    def test_model_schedule(self):
        """test to validate the Schedule model"""

        # request for the initial number of Schedule objects
        total_count_obj = Schedule.objects.all().count()

        # checking the number of Schedule objects
        self.assertEqual(0, total_count_obj)

        # request fields of the Schedule object
        self.schedule = Schedule.objects.create(
            schedule_name=self.name_schedule,
            student=self.student,
            faculty=self.new_faculty,
            departament=self.new_departament,
            studygroups=self.new_studygroup,
            day=self.day,
            available=True,
        )
        self.assertEqual(self.schedule.schedule_name, self.name_schedule)
        self.assertEqual(self.schedule.student, self.student)
        self.assertEqual(self.schedule.faculty, self.new_faculty)
        self.assertEqual(self.schedule.departament, self.new_departament)
        self.assertEqual(self.schedule.studygroups, self.new_studygroup)
        self.assertEqual(self.schedule.day, self.day)
        self.assertEqual(self.schedule.available, True)

        # request lessons count
        self.assertEqual(self.schedule.lessons.count(), 0)
        # add lessons
        self.schedule.lessons.add(self.new_lesson)
        # request lessons count
        self.assertEqual(self.schedule.lessons.count(), 1)

        # request for the number of Schedule objects after creating a new one and check
        now_total_count_obj = Schedule.objects.all().count()
        now_total_count_obj2 = Schedule.objects.filter(
            schedule_name=self.name_schedule).filter(student=self.student).filter(day=self.day).count()
        self.assertEqual(now_total_count_obj, total_count_obj + 1)
        self.assertEqual(now_total_count_obj2, total_count_obj + 1)

        # request from the database and check for new Schedule
        get_schedule = Schedule.objects.get(
            schedule_name=self.name_schedule, student=self.student, day=self.day)
        self.assertEqual(get_schedule.schedule_name, self.name_schedule)
        self.assertEqual(get_schedule.student, self.student)
        self.assertEqual(get_schedule.day, self.day)
