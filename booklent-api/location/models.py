from django.db import models

# Create your models here.
class Location(models.Model):
    loc_id = models.AutoField(primary_key=True)
    town = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pincode = models.IntegerField()
    # u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'location'



class Loc(models.Model):
    loc_id = models.AutoField(primary_key=True)
    latitude = models.CharField(max_length=45)
    longitude = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'loc'
