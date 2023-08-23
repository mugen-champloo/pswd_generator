from django.db import models


class Password(models.Model):
    generated_pswd = models.CharField(max_length=301, verbose_name='Сгенерированный пароль')

    def __str__(self):
        return self.generated_pswd