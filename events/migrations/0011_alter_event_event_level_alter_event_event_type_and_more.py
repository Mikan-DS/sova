# Generated by Django 4.1.6 on 2023-02-10 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_shedule_begin_alter_shedule_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.eventlevel', verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.eventtype', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event', verbose_name='Мероприятие'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.month', verbose_name='Месяц'),
        ),
    ]
