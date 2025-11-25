from django.db import models

# Create your models here.
class laptop(models.Model):
    password = models.CharField(max_length=50)
    retype_password = models.CharField(max_length=50)
    laptop = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    about = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    Checkbox = models.CharField(max_length=50)
    files = models.CharField(max_length=50)
    ram = models.IntegerField()
    ssd = models.CharField(max_length=50)
    youtube_channal= models.BooleanField(max_length=50)
