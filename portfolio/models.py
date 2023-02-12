from django.db import models
from events.models import EventLevel, Shedule
from users.models import Student


class Nomination(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название")
    def __str__(self):
        return self.title

class Achievement(models.Model):
    event_level = models.ForeignKey(EventLevel, models.CASCADE, verbose_name='Уровень')
    nomination = models.ForeignKey('Nomination', models.CASCADE, verbose_name='Номинация')
    score = models.IntegerField(verbose_name='Баллы')

    def __str__(self):
        return "%s %s (%d)"%(self.event_level, self.nomination, self.score)


class EventRole(models.Model):
    title = models.CharField(max_length=35, verbose_name="Название")
    def __str__(self):
        return self.title

class Activity(models.Model):
    shedule = models.ForeignKey(Shedule, models.CASCADE, verbose_name='Расписание')
    student = models.ForeignKey(Student, models.CASCADE, verbose_name='Студент')
    event_role = models.ForeignKey('EventRole', models.CASCADE, verbose_name='Ответсвенность')
    def __str__(self):
        return '"%s": %s (%s)'%(self.shedule.plan, self.student, self.event_role)


class DocumentType(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название")
    def __str__(self):
        return self.title

def get_user_path(instance, path):
    return "portfolio/%s/%s"%(instance.activity.student.pk, path)
class Document(models.Model):
    activity = models.ForeignKey('Activity', models.CASCADE, verbose_name='Участие')
    document_type = models.ForeignKey('DocumentType', models.CASCADE, verbose_name='Тип документа')
    image = models.ImageField(upload_to=get_user_path)
    achievement = models.ForeignKey('Achievement', models.CASCADE, verbose_name='Достижение')
    added_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время добавления")

    def __str__(self):
        if self.activity:

            return "%s - %s"%(self.activity, self.document_type)
        else:
            return "%s (%s)"%(self.document_type, self.added_date.strftime("%d/%m/%Y"))