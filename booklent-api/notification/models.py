from django.db import models
from user_post.models import UserPost
# Create your models here.
class Notification(models.Model):
    noti_id = models.AutoField(primary_key=True)
    notification = models.CharField(max_length=45)
    book = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'notification'
