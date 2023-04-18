"""
This module provides functions for calculating the area and circumference of a circle.
"""
from django.db import models

# Create your models here.

class Company(models.Model):
    """
    Calculate the area of a circle with the given radius.
    """
    cName = models.CharField(primary_key='true', max_length=50, unique='true')
    cEmail = models.EmailField()
    cLogo = models.ImageField(upload_to="images", blank=True)
    cUrl = models.CharField(max_length=50)
    class Meta:
        """
        Calculate the area of a circle with the given radius.
        """
        db_table = "company"

class Employee(models.Model):
    """
    Calculate the area of a circle with the given radius.
    """
    eFname = models.CharField(primary_key='true', max_length=50, unique='true')
    eLname = models.CharField(max_length=50)
    eCompany = models.ForeignKey(Company, on_delete=models.CASCADE)
    eEmail = models.EmailField()
    ePhone = models.CharField(max_length=50)
    class Meta:
        """
        Calculate the area of a circle with the given radius.
        """
        db_table = "employee"
    
#class Login(models.Model):
    #UserName = models.CharField(max_length=50)
    #password = models.CharField(max_length=32)
    #class Meta:
        #db_table = "login"


