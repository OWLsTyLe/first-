from django.db import models

class Category(models.Model):
    name_you = models.CharField('Ваше імʼя', max_length=100)
    name = models.CharField('Назва обʼяви', max_length=100)
    pud_text = models.TextField('Введіть текст', max_length=10000)
    pub_date = models.DateTimeField('date published')
    def  __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Додати'
        verbose_name_plural = 'Додати'