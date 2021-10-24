from django.test import TestCase
from django.core.cache import cache

from apps.university.models import Faculties, Departaments, StudyGroups, Auditories, Disciplines


class FacultiesTest(TestCase):
    """Common tests to validate the Faculties model"""

    def setUp(self):
        """Fixtures"""
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

        self.new_faculty = Faculties.objects.create(name=self.name_faculty, slug=self.slug_faculty, )
        self.new_departament = Departaments.objects.create(
            faculty=self.new_faculty,
            name=self.name_departament,
            slug=self.slug_departament,
        )

        # clear cache before running tests
        cache.clear()

    def test_model_faculties(self):
        """test to validate the Faculties model"""

        # request initial number of objects Faculties
        total_count_obj = Faculties.objects.all().count()

        # checking the number of objects Faculties
        self.assertEqual(1, total_count_obj)

        # request fields of Faculties
        self.assertEqual(self.new_faculty.name, self.name_faculty)
        self.assertEqual(self.new_faculty.slug, self.slug_faculty)

        # request for the number of Faculties objects after creating a new one and check
        now_total_count_obj = Faculties.objects.all().count()
        now_total_count_obj2 = Faculties.objects.filter(name=self.name_faculty).filter(slug=self.slug_faculty).count()
        self.assertEqual(now_total_count_obj, total_count_obj)
        self.assertEqual(now_total_count_obj2, total_count_obj)

        # request from database and check new Faculties
        get_faculty = Faculties.objects.get(name=self.name_faculty, slug=self.slug_faculty,)
        self.assertEqual(get_faculty.name, self.name_faculty)
        self.assertEqual(get_faculty.slug, self.slug_faculty)


class DepartamentsTest(FacultiesTest):
    """Common tests to validate the Departaments model"""

    def test_model_departaments(self):
        """test to validate the Departaments model"""

        # request for the initial number of Departaments objects
        total_count_obj = Departaments.objects.all().count()

        # checking the number of Departaments objects
        self.assertEqual(1, total_count_obj)

        # request fields of the Departaments object
        self.assertEqual(self.new_departament.faculty, self.new_faculty)
        self.assertEqual(self.new_departament.name, self.name_departament)
        self.assertEqual(self.new_departament.slug, self.slug_departament)

        # request for the number of Departaments objects after creating a new one and check
        now_total_count_obj = Departaments.objects.all().count()
        now_total_count_obj2 = Departaments.objects.filter(
            faculty=self.new_faculty).filter(name=self.name_departament).filter(slug=self.slug_departament).count()
        self.assertEqual(now_total_count_obj, total_count_obj)
        self.assertEqual(now_total_count_obj2, total_count_obj)

        # request from the database and check for new Departaments
        get_departament = Departaments.objects.get(
            faculty=self.new_faculty, name=self.name_departament, slug=self.slug_departament)
        self.assertEqual(get_departament.faculty, self.new_faculty)
        self.assertEqual(get_departament.name, self.name_departament)
        self.assertEqual(get_departament.slug, self.slug_departament)


class StudyGroupsTest(DepartamentsTest):
    """Common tests to validate the StudyGroups model"""

    def test_model_studygroups(self):
        """test to validate the StudyGroups model"""

        # query for the initial number of StudyGroups objects
        total_count_obj = StudyGroups.objects.all().count()

        # checking the number of StudyGroups objects
        self.assertEqual(0, total_count_obj)

        # query the fields of the StudyGroups object
        self.new_studygroup = StudyGroups.objects.create(
            departament=self.new_departament,
            name=self.name_studygroup,
            slug=self.slug_studygroup,
        )
        self.assertEqual(self.new_studygroup.departament, self.new_departament)
        self.assertEqual(self.new_studygroup.name, self.name_studygroup)
        self.assertEqual(self.new_studygroup.slug, self.slug_studygroup)

        # query for the number of StudyGroups objects after creating a new one and check
        now_total_count_obj = StudyGroups.objects.all().count()
        now_total_count_obj2 = StudyGroups.objects.filter(
            departament=self.new_departament).filter(name=self.name_studygroup).filter(slug=self.slug_studygroup).count()
        self.assertEqual(now_total_count_obj, total_count_obj + 1)
        self.assertEqual(now_total_count_obj2, total_count_obj + 1)

        # request from the database and check the new StudyGroups
        get_studygroup = StudyGroups.objects.get(
            departament=self.new_departament, name=self.name_studygroup, slug=self.slug_studygroup)
        self.assertEqual(get_studygroup.departament, self.new_departament)
        self.assertEqual(get_studygroup.name, self.name_studygroup)
        self.assertEqual(get_studygroup.slug, self.slug_studygroup)


class AuditoriesTest(StudyGroupsTest):
    """Common tests to validate the Auditories model"""

    def test_model_auditories(self):
        """test to validate the Auditories model"""

        # request the initial number of Auditories objects
        total_count_obj = Auditories.objects.all().count()

        # checking the number of Auditories objects
        self.assertEqual(0, total_count_obj)

        # request fields of the Auditories object
        self.new_auditory = Auditories.objects.create(name=self.name_auditory, slug=self.slug_auditory,)

        self.assertEqual(self.new_auditory.name, self.name_auditory)
        self.assertEqual(self.new_auditory.slug, self.slug_auditory)

        # request for the number of Auditories objects after creating a new one and check
        now_total_count_obj = Auditories.objects.all().count()
        now_total_count_obj2 = Auditories.objects.filter(name=self.name_auditory).filter(slug=self.slug_auditory).count()
        self.assertEqual(now_total_count_obj, total_count_obj + 1)
        self.assertEqual(now_total_count_obj2, total_count_obj + 1)

        # request from the database and check for new Auditories
        get_auditory = Auditories.objects.get(name=self.name_auditory, slug=self.slug_auditory)
        self.assertEqual(get_auditory.name, self.name_auditory)
        self.assertEqual(get_auditory.slug, self.slug_auditory)


class DisciplinesTest(AuditoriesTest):
    """Common tests to validate the Disciplines model"""

    def test_model_disciplines(self):
        """test to validate the Disciplines model"""

        # request for the initial number of objects Disciplines
        total_count_obj = Disciplines.objects.all().count()

        # checking the number of objects Disciplines
        self.assertEqual(0, total_count_obj)

        # request fields of object Disciplines
        self.new_discipline = Disciplines.objects.create(name=self.name_discipline, slug=self.slug_discipline,)

        self.assertEqual(self.new_discipline.name, self.name_discipline)
        self.assertEqual(self.new_discipline.slug, self.slug_discipline)

        # request for the number of Disciplines objects after creating a new one and check
        now_total_count_obj = Disciplines.objects.all().count()
        now_total_count_obj2 = Disciplines.objects.filter(name=self.name_discipline).filter(slug=self.slug_discipline).count()
        self.assertEqual(now_total_count_obj, total_count_obj + 1)
        self.assertEqual(now_total_count_obj2, total_count_obj + 1)

        # request from the database and check for new Disciplines
        get_discipline = Disciplines.objects.get(name=self.name_discipline, slug=self.slug_discipline)
        self.assertEqual(get_discipline.name, self.name_discipline)
        self.assertEqual(get_discipline.slug, self.slug_discipline)
