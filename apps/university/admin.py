from django.contrib import admin
from .models import Faculties, Departaments, StudyGroups, Auditories, Disciplines


class FacultiesAdmin(admin.ModelAdmin):
    """***"""

    list_display = ('name', 'slug')
    list_display_links = ('name',)
    ordering = ('-name',)
    fieldsets = ()
    prepopulated_fields = {'slug': ('name',)}


class DepartamentsAdmin(admin.ModelAdmin):
    """***"""

    list_display = ('name', 'slug')
    list_display_links = ('name',)
    ordering = ('-name',)
    fieldsets = ()
    prepopulated_fields = {'slug': ('name',)}


class StudyGroupsAdmin(admin.ModelAdmin):
    """***"""

    list_display = ('name', 'slug')
    list_display_links = ('name',)
    ordering = ('-name',)
    fieldsets = ()
    prepopulated_fields = {'slug': ('name',)}


class AuditoriesAdmin(admin.ModelAdmin):
    """***"""

    list_display = ('name', 'slug')
    list_display_links = ('name',)
    ordering = ('-name',)
    fieldsets = ()
    prepopulated_fields = {'slug': ('name',)}


class DisciplinesAdmin(admin.ModelAdmin):
    """***"""

    list_display = ('name', 'slug')
    list_display_links = ('name',)
    ordering = ('-name',)
    fieldsets = ()
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Faculties, FacultiesAdmin)
admin.site.register(Departaments, DepartamentsAdmin)
admin.site.register(StudyGroups, StudyGroupsAdmin)
admin.site.register(Auditories, AuditoriesAdmin)
admin.site.register(Disciplines, DisciplinesAdmin)
