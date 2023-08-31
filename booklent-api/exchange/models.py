from django.db import models

# Create your models here.
class Exchange(models.Model):
    exc_id = models.AutoField(primary_key=True)
    usr_bk_nm = models.CharField(max_length=45)
    book_of_exch = models.CharField(max_length=45)
    owner = models.CharField(max_length=45)
    exch_date = models.DateField()
    usr_nm = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'exchange'
