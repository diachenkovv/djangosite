from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст новини')
    date = models.DateTimeField('Дата та час публікації')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/news/{self.id}'

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
