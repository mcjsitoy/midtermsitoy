from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length =100)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    content = models.TextField(max_length = 200)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    date_created = models.DateTimeField('date created')
    content = models.TextField(max_length = 200)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments', null=True, blank=True)
