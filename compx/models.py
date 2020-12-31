from django.db import models
from django.urls import reverse

# Create your models here.

class ModelWithFileField(models.Model):
    fname_field = models.CharField(max_length=30,default='solve')
    code_field = models.TextField(default="not found")
    complexity_field = models.CharField(max_length=30,default='logarithmic')

