# Generated by Django 2.2.6 on 2019-10-30 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacseenApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccine',
            name='vaccine_taken_date',
        ),
    ]
