# Generated by Django 3.0.1 on 2021-07-06 05:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Тут должно быть название', max_length=50)),
                ('description', models.TextField(default='Тут должно быть описание')),
                ('date', models.DateField(default=datetime.datetime(2021, 7, 6, 8, 48, 17, 140860))),
                ('preview', models.ImageField(upload_to='')),
            ],
        ),
    ]
