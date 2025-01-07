from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Organization)

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'organization', 'schedule', 'author')
    list_filter = ('type', 'organization', 'schedule')
    search_fields = ('title', 'description', 'author__name', 'organization__name')
    readonly_fields = ('author',)
    filter_horizontal = ('participants',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_submitted')
    list_filter = ('date_submitted',)
    search_fields = ('title', 'body', 'author__name')
    readonly_fields = ('date_submitted',)
