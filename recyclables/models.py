from django.contrib.auth.models import User
from django.db import models
from users.models import Student

class RecyclableType(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    def __str__(self):
        return self.title

class RecyclableLog(models.Model):
    student = models.ForeignKey(Student, models.CASCADE, verbose_name="Студент")
    count = models.IntegerField(verbose_name="Количество")
    recyclable_type = models.ForeignKey('RecyclableType', models.CASCADE, verbose_name="Тип вторсырья")
    log_time = models.DateField(auto_now=True)
    moderator = models.ForeignKey(User, models.CASCADE, verbose_name="Принявший")
    def __str__(self):
        return "%s:%s (%s) - %s" % (self.recyclable_type, self.count, self.log_time, self.student)
