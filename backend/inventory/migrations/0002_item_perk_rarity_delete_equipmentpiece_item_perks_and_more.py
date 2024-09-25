# Generated by Django 5.1.1 on 2024-09-25 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('gear_score', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('allowed_item_types', models.CharField(choices=[('headwear', 'Helmet'), ('headwear', 'Helmet'), ('chestwear', 'Chest'), ('glove', 'Gloves'), ('legwaer', 'Legs'), ('footwear', 'Boots'), ('primary_weapon', 'Primary Weapon'), ('secondary_weapon', 'Secondary Weapon')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='EquipmentPiece',
        ),
        migrations.AddField(
            model_name='item',
            name='perks',
            field=models.ManyToManyField(to='inventory.perk'),
        ),
        migrations.AddField(
            model_name='item',
            name='rarity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.rarity'),
        ),
    ]