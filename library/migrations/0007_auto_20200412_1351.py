# Generated by Django 3.0.5 on 2020-04-12 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20200409_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuedbook',
            name='Mail_ID',
        ),
        migrations.RemoveField(
            model_name='issuedbook',
            name='isbn',
        ),
    ]
