from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    created_by = models.ForeignKey(User , on_delete=models.CASCADE , blank=False , null=True)
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=800)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
