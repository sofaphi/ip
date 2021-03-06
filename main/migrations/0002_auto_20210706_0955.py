# Generated by Django 3.0.1 on 2021-07-06 06:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Тут должно быть название', max_length=50)),
                ('description', models.TextField(default='Тут должно быть описание')),
                ('dateStart', models.DateField(default=datetime.datetime(2021, 7, 6, 9, 55, 30, 928176))),
                ('dateEnd', models.DateField(default=datetime.datetime(2021, 7, 6, 9, 55, 30, 928176))),
                ('preview', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Tourtaiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Тут должно быть название', max_length=50)),
                ('description', models.TextField(default='Тут должно быть описание')),
                ('date', models.DateField(default=datetime.datetime(2021, 7, 6, 9, 55, 30, 929175))),
                ('place', models.PositiveSmallIntegerField(default=1)),
                ('preview', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Тут должно быть название', max_length=50)),
                ('description', models.TextField(default='Тут должно быть описание')),
                ('dateStart', models.DateField(default=datetime.datetime(2021, 7, 6, 9, 55, 30, 927175))),
                ('dateEnd', models.DateField(default=datetime.datetime(2021, 7, 6, 9, 55, 30, 927175))),
                ('preview', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='certificate',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 6, 9, 55, 30, 926175)),
        ),
    ]
