from config.celery import app
from django.core.mail import send_mail


@app.task
def sent_schedule(username_for_request, id_for_request, email, count_lessons, lessons, day):

    subject = f'Your schedule for {day}'
    message = f'Dear {username_for_request}, id: {id_for_request}. Your schedule for {day}! Lessons today: {count_lessons}. Lessons: {lessons}'
    mail_sent = send_mail(subject, message, 'info@university-schedule.com', [email])

    return mail_sent
