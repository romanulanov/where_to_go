from django.db import models

class Coordinate(models.Model):
    models.FloatField(verbose_name='Широта')
    models.FloatField(verbose_name='Долгота')

class Place(models.Model):
    title = models.CharField(max_length=50)
    imgs = models.ImageField(upload_to='images',
                              null=True,
                              blank=True,
                              verbose_name='Картинка')
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates = models.ForeignKey(Coordinate, on_delete=models.CASCADE, verbose_name='Координаты')
                                   

