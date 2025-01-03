from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=155,verbose_name='Заголовок')
    image = models.ImageField(upload_to='settings', verbose_name='Фото')
    description_image = models.TextField(verbose_name='Описание фотографий')
    title2 = models.CharField(max_length=155,verbose_name='Заголовок 2')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Настройки Главной Страницы'

class Settings_All(models.Model):
    title = models.CharField(max_length=155,verbose_name='Заголовок')
    static = models.IntegerField(verbose_name='Статистика')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Статистика в Главном Странице'

class News(models.Model):
    image = models.ImageField(upload_to='news', verbose_name='Фото')
    title = models.CharField(max_length=155,verbose_name='Заголовок')
    title2 = models.CharField(max_length=155,verbose_name='Заголовок 2')
    title3 = models.CharField(max_length=155,verbose_name='Заголовок 3')
    text1 = models.TextField(verbose_name='Описание 1')
    text2 = models.TextField(verbose_name='Описание 2')

    image2 = models.ImageField(upload_to='news', verbose_name='Фото 2')
    title4  = models.CharField(max_length=155,verbose_name='Заголовок 4')
    title5 = models.CharField(max_length=155,verbose_name='Заголовок 5')
    title6 = models.CharField(max_length=155,verbose_name='Заголовок 6')
    text3 = models.TextField(verbose_name='Описание 3')
    text4 = models.TextField(verbose_name='Описание 4')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'