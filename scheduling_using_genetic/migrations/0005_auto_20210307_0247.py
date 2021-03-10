# Generated by Django 3.1.7 on 2021-03-06 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling_using_genetic', '0004_auto_20210304_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingtime',
            name='time',
            field=models.CharField(choices=[('7:30 - 9:30', '7:30 - 9:30'), ('9:30 - 11:30', '9:30 - 11:30'), ('1:00 - 3:00', '1:00 - 3:00'), ('3:00 - 5:00', '3:00 - 5:00')], default='11:30 - 12:30', max_length=50),
        ),
    ]
