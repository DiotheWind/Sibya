from django.contrib import admin
from .models import User, Organization, Notice

# Register your models here.
admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Notice)
