# Generated by Django 5.1.4 on 2025-01-09 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sibya', '0009_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
    ]
