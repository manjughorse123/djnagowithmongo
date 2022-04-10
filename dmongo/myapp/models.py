from django.db import models

# Create your models here.
class Depastment(models.Model):
    depastment_name = models.CharField(max_length=255)


class Employee(models.Model):

    dateof_joining = models.DateTimeField(auto_now_add=True)
    
    employee_name = models.CharField(max_length=255)
    depastment = models.CharField(max_length=255)


