from django.db import models
from django.urls import reverse


def update_model_from_dict(model: models.Model, values: dict):
    for var in values.keys():
        model.__setattr__(var, values[var])


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
    event_type = models.ForeignKey('EventType', models.CASCADE, verbose_name="Тип")
    event_level = models.ForeignKey('EventLevel', models.CASCADE, verbose_name="Уровень")
    weorg = models.BooleanField(default=True, verbose_name="Организатор")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', kwargs={'event_id': self.pk})


class Month(models.Model):
    title = models.CharField(max_length=9, verbose_name="Название")

    def __str__(self):
        return self.title


class Plan(models.Model):
    event = models.ForeignKey('Event', models.CASCADE, verbose_name="Мероприятие")
    month = models.ForeignKey('Month', models.CASCADE, verbose_name="Месяц")
    year = models.IntegerField(verbose_name="Год")

    def __str__(self):
        return str(self.event) + ": " + str(self.year) + " " + str(self.month)

    def get_absolute_url(self):
        return reverse('plan', kwargs={'event_id': self.event.pk, 'plan_id': self.pk})


class Shedule(models.Model):
    plan = models.OneToOneField('Plan', models.CASCADE, verbose_name="План")
    begin = models.DateField(verbose_name='Дата начала')
    end = models.DateField(verbose_name='Дата конца')

    def __str__(self):
        if self.begin == self.end:
            return "Дата: %s" % self.begin.strftime("%m/%d/%Y")
        else:
            return "Дата начала: %s Дата конца: %s"%(self.begin.strftime("%m/%d/%Y"), self.end.strftime("%m/%d/%Y"))


class Report(models.Model):

    title = models.CharField(max_length=60, verbose_name="Название")
    shedule = models.ForeignKey('Shedule', models.CASCADE, verbose_name='Расписание')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', editable=False)
    edited_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('report', kwargs={'report_id': self.pk})


class ReportImage(models.Model):

    report = models.ForeignKey('Report', models.CASCADE, verbose_name='Отчет')
    image = models.ImageField(upload_to="reports/%Y/%m/%d/", verbose_name='Изображение')
