from distutils.command.upload import upload
from django.db import models
# Create your models here.


class State(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    pic = models.ImageField(upload_to="myimage", default="")
