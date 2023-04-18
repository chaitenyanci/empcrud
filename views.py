"""
This module provides functions for views.
"""
from django.shortcuts import render, redirect
from mirai.models import Company, Employee
from mirai.forms import CompanyForm, EmployeeForm

def home(request):
    """
    Calculate the area of a circle with the given radius.
    """
    return redirect(request, "")
# To create Company
def comp(request):
    """
    Calculate the area of a circle with the given radius.
    """
    if request.method == "POST":

        form = CompanyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = CompanyForm()
    return render(request, "index.html", {'form':form})
# To retrieve Company details
def show(request):
    """
    Calculate the area of a circle with the given radius.
    """
    companies = Company.objects.all()
    return render(request, "show.html", {'companies':companies})
# To Edit Company details
def edit(request, cName):
    """
    Calculate the area of a circle with the given radius.
    """
    company = Company.objects.get(cName=cName)
    return render(request, "edit.html", {'company':company})
# To Update Company
def update(request, cName):
    """
    Calculate the area of a circle with the given radius.
    """
    company = Company.objects.get(cName=cName)
    form = CompanyForm(request.POST, instance=company)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "edit.html", {'company': company})
# To Delete Company details
def delete(request, cName):
    """
    Calculate the area of a circle with the given radius.
    """
    company = Company.objects.get(cName=cName)
    company.delete()
    return redirect("/show")
# To create employee
def emp(request):
    """
    Calculate the area of a circle with the given radius.
    """
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/showemp")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "addemp.html", {'form':form})
# To show employee details
def showemp(request):
    """
    Calculate the area of a circle with the given radius.
    """
    employees = Employee.objects.all()
    return render(request, "showemp.html", {'employees':employees})
# To delete employee details
def deleteEmp(request, eFname):
    """
    Calculate the area of a circle with the given radius.
    """
    employee = Employee.objects.get(eFname=eFname)
    employee.delete()
    return redirect("/showemp")
# To edit employee details
def editemp(request, eFname):
    """
    Calculate the area of a circle with the given radius.
    """
    employee = Employee.objects.get(eFname=eFname)
    return render(request, "editemployee.html", {'employee':employee})
# To update employee details
def updateEmp(request, eFname):
    """
    Calculate the area of a circle with the given radius.
    """
    employee = Employee.objects.get(eFname=eFname)
    form = EmployeeForm(request.POST, instance=employee)
    print('Hello1')
    if form.is_valid():
        form.save()
        return redirect("/showemp")
    return render(request, "editemployee.html", {'employee': employee})
    