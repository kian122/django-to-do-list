from django.db import models

# Create your models here.

class To_do(models.Model):
    name = models.CharField(max_length=80)
    decription = models.TextField(max_length=800)
    time = models.TimeField(auto_now_add=True)
