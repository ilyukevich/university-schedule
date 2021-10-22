from django.contrib import admin
from .models import Lessons, Schedule


class LessonsAdmin(admin.ModelAdmin):
    """***"""

    list_display = ('auditory', 'lesson_name', 'day', 'time', 'created', 'updated',)
    list_display_links = ('lesson_name',)
    ordering = ('-created',)
    #fieldsets = ()


# class LessonsInline(admin.TabularInline):
#     model = Lessons
#     #extra = 1


class ScheduleAdmin(admin.ModelAdmin):
    """***"""

    list_display = ('schedule_name', 'student', 'faculty', 'departament', 'studygroups', 'day',
                    'available', 'created', 'updated',)
    list_display_links = ('schedule_name',)
    ordering = ('-created',)
    #fieldsets = ()
    #inlines = [LessonsInline]


admin.site.register(Lessons, LessonsAdmin)
admin.site.register(Schedule, ScheduleAdmin)
