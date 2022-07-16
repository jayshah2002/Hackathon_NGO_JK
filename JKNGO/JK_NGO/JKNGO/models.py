import email
from django.db import models
# Create your models here.
class person(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=10)
    email=models.EmailField(max_length=254)
    city=models.CharField(max_length=20)
    
class cloth(models.Model):
    name =models.CharField(max_length=20);
    email=models.EmailField(max_length=254);
    min_age=models.IntegerField();
    max_age=models.IntegerField();
    gender=models.CharField(max_length=100);

    
class rupees(models.Model):
    name =models.CharField(max_length=20);
    email=models.EmailField(max_length=254)
    cardno=models.IntegerField();
    month=models.IntegerField();
    year=models.IntegerField();
    cvv=models.IntegerField();
    rupee=models.IntegerField();
    
    
class food(models.Model):
    name =models.CharField(max_length=20);
    email=models.EmailField(max_length=254);
    date=models.DateField();
    time=models.TimeField();
    address=models.CharField(max_length=500);
    
class plant(models.Model):
    name=models.CharField(max_length=200);
    email=models.EmailField(max_length=254);
    address=models.CharField(max_length=500);
    plant_name=models.CharField(max_length=200);
    
    
    
