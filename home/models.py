from django.db import models

# Create your models here.
class Task(models.Model):
    Task_name = models.CharField(max_length=30)
    Task_desc = models.CharField(max_length=30)

    def __str__(self):
        return self.Task_name