from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=40, null=False)
    GENERO_TYPE = {
        ('A', 'Acción'),
        ('C', 'Comedia'),
        ('D', 'Drama'),
        ('I', 'Infantil'),
        ('T', 'Terror'),
    }
    genre = models.CharField(max_length=30, choices=GENERO_TYPE, null=False)
    movie_director = models.CharField(max_length=60, null=False)
    publication_year = models.IntegerField(null=False)
    sinopsis = models.TextField(max_length=250, null=False)
    
    def __str__(self) -> str:
        return self.title

