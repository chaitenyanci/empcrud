"""
This module provides functions for calculating the area and circumference of a circle.
"""
from django import forms
from mirai.models import Employee
from mirai.models import Company
# This is for employee
class EmployeeForm(forms.ModelForm):
    """
    Calculate the area of a circle with the given radius.
    """
    class Meta:
        """
    Calculate the area of a circle with the given radius.
    """
        model = Employee
        fields = "__all__"
#this is for company
class CompanyForm(forms.ModelForm):
    """
    Calculate the area of a circle with the given radius.
    """
    class Meta:
        """
    Calculate the area of a circle with the given radius.
    """
        model = Company
        fields = "__all__"