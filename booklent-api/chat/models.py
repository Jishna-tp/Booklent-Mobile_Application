from django.db import models
from register.models import Register
from user_post.models import UserPost
# Create your models here.
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=45)
    user_id = models.IntegerField()
    rec=models.ForeignKey(Register,on_delete=models.CASCADE)
    # rec_id = models.IntegerField()
    # book_id = models.IntegerField()
    book=models.ForeignKey(UserPost,on_delete=models.CASCADE)
    type = models.CharField(max_length=45)
    first_msg = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'chat'
