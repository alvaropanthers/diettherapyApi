# Generated by Django 3.2.4 on 2021-07-25 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='physicalactivity',
            name='activityType',
            field=models.CharField(default='hobbies', max_length=200),
        ),
    ]