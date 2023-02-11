from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name="Пользователь")
    content = models.TextField(verbose_name="Текст сообщения")
    by_moderator = models.BooleanField(verbose_name="Отправлено модератором", default=False)
    sended_at = models.DateTimeField(verbose_name="Время отправки", auto_now=True)
