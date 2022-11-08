from distutils.command.upload import upload
from enum import auto
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length = 25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length = 25)
    description = models.TextField()

    def __str__(self):
        return self.name


# class Blogs(models.Model):
#     title = models.CharField(max_length = 25)
#     description = models.TextField()
#     author_name = models.CharField(max_length = 25)
#     image = models.ImageField(upload_to='blog' ,blank =True , null = True)
#     timestamp = models.DateTimeField(auto_now_add=True ,blank=True )

#     def __str__(self):
#         return self.title