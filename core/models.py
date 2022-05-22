from distutils.command.upload import upload
from django.db import models
# Create your models here.


class State(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    pic = models.ImageField(upload_to="myimage", default="")
class Pollution(models.Model):
    City=models.CharField(max_length=150)
    Date=models.CharField(max_length=50)
    Pm2=models.FloatField()
    Pm10=models.FloatField()
    No=models.FloatField()
    No2=models.FloatField()
    Nox=models.FloatField()
    Nh3=models.FloatField()
    Co=models.FloatField()
    So2=models.FloatField()
    O3=models.FloatField()
    Benzene=models.FloatField()
    Toluene=models.FloatField()
    Xylene=models.FloatField()
    Aqi=models.FloatField()
    Air_quality=models.CharField(max_length=200)
    
