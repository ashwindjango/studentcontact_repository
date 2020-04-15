from django.db import models
from multiselectfield import MultiSelectField

class StudentData(models.Model):
    sname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    sloc = models.CharField(max_length=50)
    scontact = models.IntegerField()
    sgender=models.CharField(max_length=50)
# Create your models here.
