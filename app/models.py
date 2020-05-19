from django.db import models

# Create your models here.


class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    duration = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    ratings = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
