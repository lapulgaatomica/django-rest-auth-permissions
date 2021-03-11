from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    paragraph = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.paragraph[:20]
