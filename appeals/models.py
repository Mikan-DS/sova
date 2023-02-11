from django.contrib.auth import models as auth_models
from django.db import models

class Message(models.Model):
    user = models.ForeignKey(auth_models.User, models.CASCADE, verbose_name="Пользователь")
    content = models.TextField(verbose_name="Текст сообщения")
    by_moderator = models.BooleanField(verbose_name="Отправлено модератором", default=False)
    sended_at = models.DateTimeField(verbose_name="Время отправки", auto_now=True)

    def __str__(self):
        return ("to" if self.by_moderator else "from") + " " + str(self.user) + ": "+self.content[:30]
