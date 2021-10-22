# Generated by Django 3.2.8 on 2021-10-22 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=30)),
                ('time', models.CharField(choices=[('08:00-10:00', '08:00-10:00'), ('10:00-12:00', '10:00-12:00'), ('12:00-14:00', '12:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00:22:00', '20:00:22:00')], max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('auditory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auditories', to='university.auditories')),
                ('lesson_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_name', to='university.disciplines')),
            ],
            options={
                'ordering': ('lesson_name',),
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_name', models.CharField(db_index=True, max_length=200)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=30)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('departament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departament', to='university.departaments')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty', to='university.faculties')),
                ('lessons', models.ManyToManyField(related_name='lessons', to='schedule.Lessons')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('studygroups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studygroup', to='university.studygroups')),
            ],
            options={
                'ordering': ('schedule_name',),
            },
        ),
    ]
