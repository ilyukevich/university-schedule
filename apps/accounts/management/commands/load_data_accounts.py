from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission
from apps.accounts.models import Account


class Command(BaseCommand):
    """Base command for load data into database"""

    help = '>>> Load data into database (creating groups and permissions for them, creating superuser, ' \
           'creating users and selecting groups for them)'
    print(help)

    def handle(self, *args, **kwargs):
        """Base command for load data into database (creating groups and permissions for them, creating superuser,
        creating users and selecting groups for them)"""

        groups_ = ['Administrators', 'Specialists', 'Lecturers', 'Students', 'Others']

        all_permission_list = (
            'Can add User', 'Can change User', 'Can delete User', 'Can view User',
            'Can add log entry', 'Can change log entry', 'Can delete log entry', 'Can view log entry',
            'Can add group', 'Can change group', 'Can delete group', 'Can view group',
            'Can add permissions', 'Can change permissions', 'Can delete permissions', 'Can view permissions',
            'Can add category', 'Can change category', 'Can delete category', 'Can view category',
            'Can add image', 'Can change image', 'Can delete image', 'Can view image',
        )

        permission_administrator_list = (
            'Can add User', 'Can change User', 'Can delete User', 'Can view User',
            'Can add group', 'Can change group', 'Can delete group', 'Can view group',
            'Can add permissions', 'Can change permissions', 'Can delete permissions', 'Can view permissions',
            'Can add category', 'Can change category', 'Can delete category', 'Can view category',
            'Can add image', 'Can change image', 'Can delete image', 'Can view image',
        )

        permission_specialist_list = (
            'Can view User',
            #'Can add category', 'Can change category', 'Can view category',
            #'Can add image', 'Can change image', 'Can view image',
        )

        permission_lecturer_list = (
            'Can view User',
            #'Can add category', 'Can change category', 'Can view category',
            #'Can add image', 'Can change image', 'Can view image',
        )

        permission_student_list = (
            'Can view User',
            #'Can add category', 'Can change category', 'Can view category',
            #'Can add image', 'Can change image', 'Can view image',
        )

        permission_other_list = (
            'Can view User',
            #'Can add category', 'Can change category', 'Can view category',
            #'Can add image', 'Can change image', 'Can view image',
        )

        # getting a list of permissions
        permission_administrators = Permission.objects.filter(name__in=permission_administrator_list)
        permission_specialists = Permission.objects.filter(name__in=permission_specialist_list)
        permission_lecturers = Permission.objects.filter(name__in=permission_lecturer_list)
        permission_students = Permission.objects.filter(name__in=permission_student_list)
        permission_others = Permission.objects.filter(name__in=permission_other_list)

        # creating groups and permissions for them
        for group in groups_:
            if group == 'Administrators':
                new_group = Group.objects.create(name=group)
                print("Creation of the 'Administrators' group... OK")
                new_group.permissions.add(*permission_administrators)
                print("Create permissions for the 'Administrators' group... OK")
                new_group.save()
            elif group == 'Specialists':
                new_group = Group.objects.create(name=group)
                print("Creation of the 'Specialists' group... OK")
                new_group.permissions.add(*permission_specialists)
                print("Create permissions for the 'Specialists' group... OK")
                new_group.save()
            elif group == 'Lecturers':
                new_group = Group.objects.create(name=group)
                print("Creation of the 'Lecturers' group... OK")
                new_group.permissions.add(*permission_lecturers)
                print("Create permissions for the 'Lecturers' group... OK")
                new_group.save()
            elif group == 'Students':
                new_group = Group.objects.create(name=group)
                print("Creation of the 'Students' group... OK")
                new_group.permissions.add(*permission_students)
                print("Create permissions for the 'Students' group... OK")
                new_group.save()
            elif group == 'Others':
                new_group = Group.objects.create(name=group)
                print("Creation of the 'Others' group... OK")
                new_group.permissions.add(*permission_others)
                print("Create permissions for the 'Others' group... OK")
                new_group.save()

        # creating superuser
        if not Account.objects.filter(username='admin').exists():
            Account.objects.create_superuser(
                email='admin@university-schedule.com',
                username='admin',
                password='admin',
                first_name='Ivan',
                last_name='Ivanovich'
            )
            print('Create superuser... OK')

        # creating users and selecting groups for them
        administrator = Account.objects.create(
            username='administrator',
            password='administrator',
            email='administrator@university-schedule.com',
            role='Administrator',
            is_staff=True,
            is_active=True
        )
        specialist = Account.objects.create(
            username='specialist',
            password='specialist',
            email='specialist@university-schedule.com',
            role='Specialist',
            is_staff=True,
            is_active=True
        )
        lecturer = Account.objects.create(
            username='lecturer',
            password='lecturer',
            email='lecturer@university-schedule.com',
            role='Lecturer',
            is_active=True
        )
        student = Account.objects.create(
            username='student',
            password='student',
            email='student@university-schedule.com',
            role='Student',
            is_active=True
        )
        other = Account.objects.create(
            username='other',
            password='other',
            email='other@university-schedule.com',
            role='Other',
            is_active=True
        )
        administrator.save()
        specialist.save()
        lecturer.save()
        student.save()
        other.save()

        print('Create users... OK')

        group_administrators = Group.objects.get(name='Administrators')
        group_specialists = Group.objects.get(name='Specialists')
        group_lecturers = Group.objects.get(name='Lecturers')
        group_students = Group.objects.get(name='Students')
        group_others = Group.objects.get(name='Others')

        # assigning users to groups
        administrator.groups.add(group_administrators)
        specialist.groups.add(group_specialists)
        lecturer.groups.add(group_lecturers)
        student.groups.add(group_students)
        other.groups.add(group_others)
        print('Assigning users to groups... OK')
