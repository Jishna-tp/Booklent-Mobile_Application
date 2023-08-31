from django.db import models

# Create your models here.
class UserPost(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(db_column='Author_name', max_length=30)  # Field name made lowercase.
    bio = models.TextField()
    gen_id = models.IntegerField()
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_post'
