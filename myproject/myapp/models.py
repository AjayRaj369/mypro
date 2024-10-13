from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    phone = models.IntegerField()


    
