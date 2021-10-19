from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group, Permission
from django.utils.html import format_html

from .models import Account, UserProfile


class AccountAdmin(UserAdmin):

    list_display = (
        'email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'role', 'is_staff', 'is_active'
    )
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ('role', 'last_login',)
    fieldsets = ()

    list_editable = ('is_active',)


class UserProfileAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'country', 'region', 'city')


class GroupAdminWithCount(GroupAdmin):
    """Class is representation of a model Group in the admin interface."""

    list_display = GroupAdmin.list_display + ('user_count',)

    @staticmethod
    def user_count(obj):
        """Count the number of users in a group."""
        return obj.user_set.count()



admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

admin.site.unregister(Group)
admin.site.register(Group, GroupAdminWithCount)
