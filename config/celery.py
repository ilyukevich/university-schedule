import os
from celery import Celery
from celery.schedules import crontab
from django.core.mail import send_mail


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    # Executes every day morning at 6:00 a.m.
    sender.add_periodic_task(
        crontab(hour=6, minute=0),
        daily_schedule_mailing.s(),
    )


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from apps.accounts.models import Account
from apps.schedule.models import Schedule
from apps.schedule.constants import DAY, TIME
from apps.university.models import Faculties, Departaments, StudyGroups, Auditories, Disciplines
from datetime import date


@app.task
def daily_schedule_mailing():
    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    today = int(date.today().weekday())

    today_schedules_count = Schedule.objects.filter(day=weekdays[today]).count()

    if today_schedules_count == 0:
        return "No lessons in this day!"

    today_schedules = Schedule.objects.filter(day=weekdays[today])
    schedule = tuple(today_schedules.values_list())

    student = Account.objects.get(id=schedule[0][2])
    username = student.username
    email = student.email

    count_lessons = Schedule.objects.get(day=weekdays[today], student=schedule[0][2]).lessons.count()
    student_lessons = Schedule.objects.get(day=weekdays[today], student=schedule[0][2]).lessons.all().values()

    subject = f'{username}, Your schedule for {weekdays[today]}, {date.today()}'
    message = f'Dear {username}. Your schedule for {weekdays[today]}, {date.today()}! ' \
              f'Amount of lessons today: {count_lessons}! ' \
              f'Faculty: {schedule[0][3]}, ' \
              f'Departament: {schedule[0][4]}, ' \
              f'Group: {schedule[0][5],}, ' \
              f'Lessons: {tuple(student_lessons)}. ' \
              f'Have a nice day!'
    mail_sent = send_mail(subject, message, 'info@university-schedule.com', [email, ])

    return mail_sent


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
