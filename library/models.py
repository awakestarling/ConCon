from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=128)

class Author(models.Model):
    name = models.CharField(max_length=128)
