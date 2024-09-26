# Generated by Django 5.1.1 on 2024-09-26 00:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_perk_allowed_item_types'),
        ('members', '0003_character_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='game_username',
            new_name='pseudo_in_game',
        ),
        migrations.RemoveField(
            model_name='character',
            name='is_war_ready',
        ),
        migrations.RemoveField(
            model_name='character',
            name='role_in_game',
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='discord_roles',
            field=models.ManyToManyField(blank=True, related_name='discord_roles', to='members.role'),
        ),
        migrations.CreateModel(
            name='CharacterRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_war_ready', models.BooleanField(default=False)),
                ('gear_score', models.IntegerField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='members.character')),
                ('chestwear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chestwear_roles', to='inventory.item')),
                ('earswear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='earswear_roles', to='inventory.item')),
                ('footwear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='footwear_roles', to='inventory.item')),
                ('gloves', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gloves_roles', to='inventory.item')),
                ('headwear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headwear_roles', to='inventory.item')),
                ('legwear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='legwear_roles', to='inventory.item')),
                ('neclace', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='necklace_roles', to='inventory.item')),
                ('primary_weapon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_weapon_roles', to='inventory.item')),
                ('rings', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rings_roles', to='inventory.item')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.role')),
                ('secondary_weapon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='secondary_weapon_roles', to='inventory.item')),
            ],
        ),
    ]
