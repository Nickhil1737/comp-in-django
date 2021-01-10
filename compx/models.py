from django.db import models
from django.urls import reverse

# Create your models here.

class ModelWithFileField(models.Model):
    fname_field = models.CharField(max_length=30,default='solve')
    code_field = models.TextField(default="not found")
    complexity_field = models.CharField(max_length=30,default='logarithmic')

    complexity_key = models.CharField(max_length=30,default='exponential')
    time1_field = models.CharField(max_length=30, default='10')
    time2_field = models.CharField(max_length=30, default='20')
    time3_field = models.CharField(max_length=30, default='30')

    def get_absolute_url(self):
        return reverse('compxdet',args=[str(self.id)])

    def __str__(self):
        return '%s' %(self.id)
