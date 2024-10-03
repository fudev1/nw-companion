# Generated by Django 5.1.1 on 2024-10-02 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('role_type', models.CharField(choices=[('discord', 'Discord Role'), ('new_world', 'New World')], max_length=50)),
            ],
        ),
    ]