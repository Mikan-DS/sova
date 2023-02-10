# Generated by Django 4.1.6 on 2023-02-10 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_delete_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(auto_now=True, verbose_name='Дата начала')),
                ('end', models.DateField(auto_now=True, verbose_name='Дата конца')),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.plan', verbose_name='План')),
            ],
        ),
    ]
