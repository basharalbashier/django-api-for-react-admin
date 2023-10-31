from django.db import models

class Contact(models.Model):
     name=models.CharField(max_length=200)
     email=models.CharField(max_length=200)
     age=models.CharField(max_length=200)
     phone=models.CharField(max_length=200)
     address=models.CharField(max_length=200)
     city=models.CharField(max_length=200)
     zipCode=models.CharField(max_length=200)
     registrarId =    models.CharField(max_length=200)    