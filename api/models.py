from django.db import models

# Create your models here.
class Employee(models.Model):
    Ename=models.CharField(max_length=34)
    EJob=models.CharField(max_length=23)
    ESal=models.FloatField(max_length=11)
    Eaddr=models.CharField(max_length=23)
    