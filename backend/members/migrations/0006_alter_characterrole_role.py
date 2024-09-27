# Generated by Django 5.1.1 on 2024-09-27 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_character_active_role_alter_characterrole_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterrole',
            name='role',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'game'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.role'),
        ),
    ]