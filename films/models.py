from django.db import models

class Film(models.Model):

    def __str__(self):
        return self.film_name
    
    film_name = models.CharField(max_length=200)
    film_description = models.CharField(max_length=500)
    film_rating = models.IntegerField()