from django.db import models

# Create your models here.
class Rent(models.Model):
    rnt_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=45)
    date = models.DateField()
    return_date = models.DateField()
    amount = models.CharField(max_length=45)
    own_name = models.CharField(max_length=45)
    boorower_name = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    u_id = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'rent'
