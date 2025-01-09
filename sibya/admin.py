from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from simple_history.admin import SimpleHistoryAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('name', 'email', 'is_president', 'is_staff', 'is_superuser')
    list_filter = ('is_president', 'is_staff', 'is_superuser')
    search_fields = ('name', 'email')
    ordering = ('email',)

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return (
                (None, {'fields': ('email', 'password')}),
                ('Personal info', {'fields': ('name',)}),
                ('Permissions', {'fields': ('is_president', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
            )
        else:
            # Staff can only edit is_president
            return (
                ('Personal info', {'fields': ('name', 'email')}),
                ('Permissions', {'fields': ('is_president',)}),
            )

    def has_add_permission(self, request):
        # Only superusers can add users
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Only superusers can delete users
        return request.user.is_superuser

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def has_add_permission(self, request):
        # Both superusers and staff can add organizations
        return True

    def has_change_permission(self, request, obj=None):
        # Both superusers and staff can edit organizations
        return True

    def has_delete_permission(self, request, obj=None):
        # Both superusers and staff can delete organizations
        return True

@admin.register(Notice)
class NoticeAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'type', 'organization', 'schedule', 'author')
    list_filter = ('type', 'organization', 'schedule')
    search_fields = ('title', 'description', 'author__name', 'organization__name')
    readonly_fields = ('author',)
    filter_horizontal = ('interested',)

    def has_add_permission(self, request):
        # Only superusers can add notices
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        # Only superusers can edit notices
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Both superusers and staff can delete notices
        return True

@admin.register(Feedback)
class FeedbackAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'author', 'date_submitted')
    list_filter = ('date_submitted',)
    search_fields = ('title', 'body', 'author__name')
    readonly_fields = ('date_submitted',)

    def has_add_permission(self, request):
        # Only superusers can add feedback
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        # Only superusers can edit feedback
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Both superusers and staff can delete feedback
        return True
