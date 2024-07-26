from django.db import models

# Create your models here.


class Publication(models.Model):

    title = models.CharField(verbose_name='название', max_length=255)
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(verbose_name='изображение')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Blog(models.Model):
    pass