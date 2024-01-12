from django.db import models

# Create your models here.

class Cosa(models.Model):
    name = models.CharField(max_length = 100, default = '')
    age = models.IntegerField(default = 0)