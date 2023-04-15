from django.db import models
from django.utils import timezone


# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

class secretClient(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    options = models.CharField(max_length=50)
    datePosted = models.DateTimeField(default=timezone.now)

