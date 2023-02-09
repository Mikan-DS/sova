from django.db import models
from django.urls import reverse


class EventType(models.Model):
    title = models.CharField(max_length=15, verbose_name="Название")
    def __str__(self):
        return self.title
class EventLevel(models.Model):
    title = models.CharField(max_length=19, verbose_name="Название")
    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    event_type = models.ForeignKey('EventType', models.SET_NULL, null=True, verbose_name="Тип")
    event_level = models.ForeignKey('EventLevel', models.SET_NULL, null=True, verbose_name="Уровень")
    weorg = models.BooleanField(default=True, verbose_name="Организатор")

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse('event', kwargs={'event_id': self.pk})



class Month(models.Model):
    title = models.CharField(max_length=9, verbose_name="Название")
    def __str__(self):
        return self.title

class Plan(models.Model):
    event = models.ForeignKey('Event', models.SET_NULL, null=True, verbose_name="Мероприятие")
    month = models.ForeignKey('Month', models.SET_NULL, null=True, verbose_name="Месяц")
    year = models.IntegerField(verbose_name="Год")

    def __str__(self):
        return "PLAN"
class Result(models.Model):
    plan = models.ForeignKey('Plan', models.SET_NULL, null=True, verbose_name="План")
    begin = models.DateField(auto_now=True, verbose_name='Дата начала')
    end = models.DateField(auto_now=True, verbose_name='Дата конца')
    peoples = models.IntegerField(verbose_name="Людей задейственно")

    def __str__(self):
        return "RESULT"