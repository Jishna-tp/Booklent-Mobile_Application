from django.db import models
from user_post.models import UserPost
# Create your models here.
class Favorite(models.Model):
    fav_id = models.AutoField(primary_key=True)
    # bk_id = models.IntegerField()
    bk=models.ForeignKey(UserPost,on_delete=models.CASCADE)
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'favorite'
