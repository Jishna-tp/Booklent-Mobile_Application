from django.db import models

# Create your models here.
class Register(models.Model):
    reg_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    interest = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'register'


