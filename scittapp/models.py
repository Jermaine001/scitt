from django.db import models

# Create your models here.
class Enrollment(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    education = models.CharField(max_length=50)
    programming = models.CharField(max_length=50)
    availability = models.CharField(max_length=100)
    computer_access = models.CharField(max_length=3)
    internet_access = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

