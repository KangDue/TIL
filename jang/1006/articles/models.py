from django.db import models
from django.conf import settings
# Create your models here.
class Article(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    maked = models.DateTimeField(auto_now_add=True)
    revised = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    maked = models.DateTimeField(auto_now_add=True)
    revised = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
    