from django.db import models
from genre.models import Genre
# Create your models here.
class UserPost(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(db_column='Author_name', max_length=30)  # Field name made lowercase.
    bio = models.TextField()
    # gen_id = models.IntegerField()
    gen=models.ForeignKey(Genre,on_delete=models.CASCADE)
    u_id = models.IntegerField()
    status = models.CharField(max_length=45)
    image = models.CharField(max_length=500)


    class Meta:
        managed = False
        db_table = 'user_post'
