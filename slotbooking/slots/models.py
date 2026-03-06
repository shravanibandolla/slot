from django.db import models

# Create your models here.
class Slot(models.Model):
    time = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="available")

    def __str__(self):
        return self.time
