from django.db import models

# Create your models here.


class Contact(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    inputEmail4 = models.CharField(max_length=120)
    floatingTextarea = models.TextField()
