# Generated by Django 5.1.1 on 2024-09-24 15:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('discord', 'Discord Role'), ('game', 'Game Role')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('discord_id', models.CharField(max_length=50, unique=True)),
                ('discord_username', models.CharField(max_length=100, unique=True)),
                ('is_invited', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('discord_roles', models.ManyToManyField(related_name='discord_roles', to='members.role')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('game_username', models.CharField(max_length=100, unique=True)),
                ('is_war_ready', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='members.memberprofile')),
                ('role_in_game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_roles', to='members.role')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]