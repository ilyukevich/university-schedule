from django.core.management.base import BaseCommand, CommandError

from apps.university.models import Faculties, Departaments, StudyGroups, Auditories, Disciplines


class Command(BaseCommand):
    """Base command for load data for app University into database"""

    help = '>>> load data for app University into database ' \
           '(Faculties, Departaments, StudyGroups, Auditories, Disciplines)'
    print(help)

    def handle(self, *args, **kwargs):
        """Base command for load data into database (loading data for the University application)"""

        # Faculties
        faculty_names = ['Faculty of Computer Design', 'Faculty of Information Technology and Management',
                         'Faculty of Radio Engineering and Electronics', 'Faculty of Computer Systems and Networks',
                         'Faculty of Infocommunications', 'Engineering and Economics Faculty']
        faculty_slugs = ['faculty-of-computer-design', 'faculty-of-information-technology-and-management',
                         'faculty-of-radio-engineering-and-electronics', 'faculty-of-computer-systems-and-networks',
                         'faculty-of-infocommunications', 'engineering-and-economics-faculty']

        # faculty_name_1 = 'Faculty of Computer Design'
        # faculty_slug_1 = 'faculty-of-computer-design'
        # faculty_name_2 = 'Faculty of Information Technology and Management'
        # faculty_slug_2 = 'faculty-of-information-technology-and-management'
        # faculty_name_3 = 'Faculty of Radio Engineering and Electronics'
        # faculty_slug_3 = 'faculty-of-radio-engineering-and-electronics'
        # faculty_name_4 = 'Faculty of Computer Systems and Networks'
        # faculty_slug_4 = 'faculty-of-computer-systems-and-networks'
        # faculty_name_5 = 'Faculty of Infocommunications'
        # faculty_slug_5 = 'faculty-of-infocommunications'
        # faculty_name_6 = 'Engineering and Economics Faculty'
        # faculty_slug_6 = 'engineering-and-economics-faculty'

        obj_faculty_1 = Faculties.objects.create(name=faculty_names[0], slug=faculty_slugs[0])
        obj_faculty_2 = Faculties.objects.create(name=faculty_names[1], slug=faculty_slugs[1])
        obj_faculty_3 = Faculties.objects.create(name=faculty_names[2], slug=faculty_slugs[2])
        obj_faculty_4 = Faculties.objects.create(name=faculty_names[3], slug=faculty_slugs[3])
        obj_faculty_5 = Faculties.objects.create(name=faculty_names[4], slug=faculty_slugs[4])
        obj_faculty_6 = Faculties.objects.create(name=faculty_names[5], slug=faculty_slugs[5])

        obj_faculty_1.save()
        obj_faculty_2.save()
        obj_faculty_3.save()
        obj_faculty_4.save()
        obj_faculty_5.save()
        obj_faculty_6.save()

        print('Create Faculties... OK')

        # Departaments
        departament_names = ['Department of Information and Computer Systems Design', 'Department of Control Systems',
                             'Department of Electronics', 'Department of Informatics',
                             'Department of Information Security', 'Department of Economics']
        departament_slugs = ['department-of-information-and-computer-systems-design', 'department-of-control-systems',
                             'department-of-electronics', 'department-of-informatics',
                             'department-of-information-security', 'department-of-economics']

        # departament_name_1 = 'Department of Information and Computer Systems Design'
        # departament_slug_1 = 'department-of-information-and-computer-systems-design'
        # departament_name_2 = 'Department of Control Systems'
        # departament_slug_2 = 'department-of-control-systems'
        # departament_name_3 = 'Department of Electronics'
        # departament_slug_3 = 'department-of-electronics'
        # departament_name_4 = 'Department of Informatics'
        # departament_slug_4 = 'department-of-informatics'
        # departament_name_5 = 'Department of Information Security'
        # departament_slug_5 = 'department-of-information-security'
        # departament_name_6 = 'Department of Economics'
        # departament_slug_6 = 'department-of-economics'

        obj_departament_1 = Departaments.objects.create(
            faculty=obj_faculty_1,
            name=departament_names[0],
            slug=departament_slugs[0]
        )
        obj_departament_2 = Departaments.objects.create(
            faculty=obj_faculty_2,
            name=departament_names[1],
            slug=departament_slugs[1]
        )
        obj_departament_3 = Departaments.objects.create(
            faculty=obj_faculty_3,
            name=departament_names[2],
            slug=departament_slugs[2]
        )
        obj_departament_4 = Departaments.objects.create(
            faculty=obj_faculty_4,
            name=departament_names[3],
            slug=departament_slugs[3]
        )
        obj_departament_5 = Departaments.objects.create(
            faculty=obj_faculty_5,
            name=departament_names[4],
            slug=departament_slugs[4]
        )
        obj_departament_6 = Departaments.objects.create(
            faculty=obj_faculty_6,
            name=departament_names[5],
            slug=departament_slugs[5]
        )

        obj_departament_1.save()
        obj_departament_2.save()
        obj_departament_3.save()
        obj_departament_4.save()
        obj_departament_5.save()
        obj_departament_6.save()

        print('Create Departaments... OK')

        # StudyGroups
        studygroup_names = ['812501', '812502', '812503', '812504', '812505', '812506']
        studygroup_slugs = ['812501', '812502', '812503', '812504', '812505', '812506']

        # studygroup_name_1 = '812501'
        # studygroup_slug_1 = '812501'
        # studygroup_name_2 = '812502'
        # studygroup_slug_2 = '812502'
        # studygroup_name_3 = '812503'
        # studygroup_slug_3 = '812503'
        # studygroup_name_4 = '812504'
        # studygroup_slug_4 = '812504'
        # studygroup_name_5 = '812505'
        # studygroup_slug_5 = '812505'
        # studygroup_name_6 = '812506'
        # studygroup_slug_6 = '812506'

        obj_studygroup_1 = StudyGroups.objects.create(
            departament=obj_departament_1,
            name=studygroup_names[0],
            slug=studygroup_slugs[0]
        )
        obj_studygroup_2 = StudyGroups.objects.create(
            departament=obj_departament_2,
            name=studygroup_names[1],
            slug=studygroup_slugs[1]
        )
        obj_studygroup_3 = StudyGroups.objects.create(
            departament=obj_departament_3,
            name=studygroup_names[2],
            slug=studygroup_slugs[2]
        )
        obj_studygroup_4 = StudyGroups.objects.create(
            departament=obj_departament_4,
            name=studygroup_names[3],
            slug=studygroup_slugs[3]
        )
        obj_studygroup_5 = StudyGroups.objects.create(
            departament=obj_departament_5,
            name=studygroup_names[4],
            slug=studygroup_slugs[4]
        )
        obj_studygroup_6 = StudyGroups.objects.create(
            departament=obj_departament_6,
            name=studygroup_names[5],
            slug=studygroup_slugs[5]
        )

        obj_studygroup_1.save()
        obj_studygroup_2.save()
        obj_studygroup_3.save()
        obj_studygroup_4.save()
        obj_studygroup_5.save()
        obj_studygroup_6.save()

        print('Create StudyGroups... OK')

        # Auditories
        for i in range(20):
            if i == 0:
                continue
            obj_auditories = Auditories.objects.create(name=i, slug=i)
            obj_auditories.save()

        print('Create Auditories... OK')

        # Disciplines
        discipline_names = ['Design', 'Management', 'Electronics', 'Networks', 'Infocommunications', 'Economics']
        discipline_slugs = ['design', 'management', 'electronics', 'networks', 'infocommunications', 'economics']

        # discipline_name_1 = 'Design'
        # discipline_slug_1 = 'design'
        # discipline_name_2 = 'Management'
        # discipline_slug_2 = 'management'
        # discipline_name_3 = 'Electronics'
        # discipline_slug_3 = 'electronics'
        # discipline_name_4 = 'Networks'
        # discipline_slug_4 = 'networks'
        # discipline_name_5 = 'Infocommunications'
        # discipline_slug_5 = 'infocommunications'
        # discipline_name_6 = 'Economics'
        # discipline_slug_6 = 'economics'

        obj_discipline_1 = Disciplines.objects.create(name=discipline_names[0], slug=discipline_slugs[0])
        obj_discipline_2 = Disciplines.objects.create(name=discipline_names[1], slug=discipline_slugs[1])
        obj_discipline_3 = Disciplines.objects.create(name=discipline_names[2], slug=discipline_slugs[2])
        obj_discipline_4 = Disciplines.objects.create(name=discipline_names[3], slug=discipline_slugs[3])
        obj_discipline_5 = Disciplines.objects.create(name=discipline_names[4], slug=discipline_slugs[4])
        obj_discipline_6 = Disciplines.objects.create(name=discipline_names[5], slug=discipline_slugs[5])

        obj_discipline_1.save()
        obj_discipline_2.save()
        obj_discipline_3.save()
        obj_discipline_4.save()
        obj_discipline_5.save()
        obj_discipline_6.save()

        print('Create Disciplines... OK')

        print('>>> Creation completed!')
