from django.db import models

# Create your models here.

class GenreSelected(models.Model):
    user_id = models.IntegerField()
    genre_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'genre_selected'
