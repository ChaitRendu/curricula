from django.db import models
from django.db import models

class people(models.Model):
    firstname=models.CharField(max_length=30)
    email=models.CharField(max_length=50)


# Create your models here.
