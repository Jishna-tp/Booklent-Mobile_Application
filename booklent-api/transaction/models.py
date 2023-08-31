from django.db import models

# Create your models here.

class Transcation(models.Model):
    tran_id = models.AutoField(primary_key=True)
    book = models.CharField(max_length=200)
    usr_nm = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'transcation'

