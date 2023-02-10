# Generated by Django 4.1.6 on 2023-02-09 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.event', verbose_name='Мероприятие'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='month',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.month', verbose_name='Месяц'),
        ),
        migrations.AlterField(
            model_name='result',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.plan', verbose_name='План'),
        ),
    ]