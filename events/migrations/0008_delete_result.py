# Generated by Django 4.1.6 on 2023-02-10 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_remove_result_peoples'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Result',
        ),
    ]
