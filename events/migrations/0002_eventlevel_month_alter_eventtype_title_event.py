# Generated by Django 4.1.6 on 2023-02-09 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=19, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=9)),
            ],
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='title',
            field=models.CharField(max_length=15, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=19, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('weorg', models.BooleanField(default=True, verbose_name='Организатор')),
                ('event_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.eventlevel', verbose_name='Уровень')),
                ('event_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.eventtype', verbose_name='Тип')),
            ],
        ),
    ]
