from django.db import models


class Place(models.Model):
    title = models.CharField(
        max_length=50,
        blank=True,
        unique=True,
        )
    short_description = models.TextField(
                              blank=True,
                              )
    long_description = models.TextField(
                              blank=True,
                              )
    lat = models.FloatField(blank=True,
                            verbose_name='Широта',
                            )
    lon = models.FloatField(blank=True,
                            verbose_name='Долгота',
                            )

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('lon', 'lat')


class Image(models.Model):
    num = models.IntegerField(default=0,
                              blank=True,
                              verbose_name='Порядковый номер',
                              )
    title = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              verbose_name='Мероприятие',
                              )
    img = models.ImageField()

    class Meta:
        ordering = ['num']

    def __str__(self):
        return self.title
