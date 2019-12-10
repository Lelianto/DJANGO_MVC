from django.db import models
from datetime import datetime

# Create your models here.

class Mentor(models.Model):
    nama = models.CharField(max_length=200, default=None)
    jabatan = models.CharField(max_length=200, default=None)
    experience = models.IntegerField(default=0)
    quote = models.CharField(max_length=200, default=None)
    img_mentor_url = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.nama

class Mentee(models.Model):
    nama = models.CharField(max_length=200, default=None)
    quote = models.CharField(max_length=200, default=None)
    img_mentee_url = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.nama

class Blog(models.Model):
    img_blog_url = models.CharField(max_length=200, default=None)
    title = models.CharField(max_length=500, default=None)
    text_content = models.TextField(default=None)
    date_post = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

    