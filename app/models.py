from django.db import models

# Create your models here.

from app.models import *

class school(models.Model):
    s_name=models.CharField(max_length=100)
    s_marks=models.CharField(max_length=100)
    