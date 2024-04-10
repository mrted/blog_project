from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs', null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

