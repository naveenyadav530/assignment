from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class SignUp(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()

    address = models.CharField(max_length=50)
    contact = PhoneNumberField()
    dob = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.name
    