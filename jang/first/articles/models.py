from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    maked = models.DateTimeField(auto_now_add=True)
    revised = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.title