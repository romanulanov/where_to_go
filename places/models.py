from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=50,
                              blank=True,
                              )
    description_short = models.TextField(
                              blank=True,
                              )
    description_long = models.TextField(
                              blank=True,
                              )
    lat = models.FloatField(blank=True,
                            null=True,
                            verbose_name='Широта',
                            )
    lon = models.FloatField(blank=True,
                            null=True,
                            verbose_name='Долгота',
                            )


    def __str__(self):
        return self.title
                                   

class Image(models.Model):
    num = models.IntegerField(default=0,
                              blank=True,
                              null=True,
                              verbose_name='Порядковый номер',
                              )
    title = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              verbose_name='Мероприятие',
                              )
    img = models.ImageField(blank=True,
                            
                            )
    
    
    class Meta:
        ordering = ['num']


    def __str__(self):
        return f'{self.title}'
