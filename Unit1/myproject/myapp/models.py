from django.db import models

# Create your models here.
class employee(models.model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()