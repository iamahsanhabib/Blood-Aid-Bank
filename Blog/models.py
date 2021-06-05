from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.aggregates import Count
from random import randint

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length =200, verbose_name="পোস্ট টাইটেল", null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="লেখক", null=False)
    image = models.ImageField(upload_to = "Post/", default="", verbose_name="ছবি")
    body1 = models.TextField(verbose_name="কন্টেন্ট ১ম অংশ")
    body2 = models.TextField(verbose_name="কন্টেন্ট ২য় অংশ")
    date = models.DateTimeField(auto_now_add=False, default=datetime.datetime.now)

    def __str__(self):
        return self.title +'|'+ str(self.author)