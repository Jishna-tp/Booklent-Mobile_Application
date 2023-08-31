from django.db import models

# Create your models here.

class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'genre'
