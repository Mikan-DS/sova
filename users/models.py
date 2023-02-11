from django.contrib.auth import models as auth_models
from django.db import models

class Specialization(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название")
    code = models.CharField(max_length=10, verbose_name="Код специальности")
    def __str__(self):
        return self.title
class Curator(models.Model):
    FIO = models.CharField(max_length=60, verbose_name="Ф.И.О.")
    number = models.CharField(max_length=15, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return self.FIO
class Group(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название")
    specialization = models.ForeignKey('Specialization', models.CASCADE, verbose_name="Специализация")
    curator = models.ForeignKey('Curator', models.CASCADE, verbose_name="Куратор")

    def __str__(self):
        return self.title
class Student(models.Model):
    group = models.ForeignKey('Group', models.CASCADE, verbose_name="Группа")
    birthday = models.DateField(verbose_name="Дата рождения")
    number = models.CharField(max_length=15, verbose_name="Номер телефона")
    user = models.OneToOneField(auth_models.User, models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(upload_to="students/", verbose_name='Фото профиля', null=True)

    def __str__(self):
        return self.user.first_name
# 1p2hj21ebv