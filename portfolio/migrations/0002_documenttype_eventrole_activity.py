# Generated by Django 4.1.6 on 2023-02-12 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_alter_report_created_at'),
        ('users', '0003_student_image'),
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='EventRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.eventrole', verbose_name='Ответсвенность')),
                ('shedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.shedule', verbose_name='Расписание')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student', verbose_name='Студент')),
            ],
        ),
    ]
