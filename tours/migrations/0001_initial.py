# Generated by Django 5.1.4 on 2024-12-20 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('guide', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='tours/')),
            ],
        ),
        migrations.CreateModel(
            name='DailyCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='tours.tour')),
            ],
        ),
    ]
