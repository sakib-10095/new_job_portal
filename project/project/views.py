from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def signupPage(request):

    if request.method=="POST":
        username=request.POST.get("username")
        display_name=request.POST.get("display_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user_type=request.POST.get("user_type")

        user=CustomUser.objects.create_user(username=username,display_name=display_name,email=email,password=password,user_type=user_type)
        user.save()
        return redirect("loginPage")
    
    return render(request,"signup.html")


def loginPage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)
        
        if user!=None:
            login(request,user)
            return redirect("DashboardPage")
    
    return render(request,"login.html")

@login_required
def DashboardPage(request):

    return render(request,"dashboard.html")

def logoutPage(request):

    logout(request)
    return redirect("loginPage")

def addjobPage(request):
    user=request.user
    if request.method=="POST":
        jobTitle=request.POST.get("jobTitle")
        companyName=request.POST.get("companyName")
        description=request.POST.get("description")
        location=request.POST.get("location")

        job=addjob_Model(jobTitle=jobTitle,companyName=companyName,description=description,location=location,job_creator=user,creat_at=user)
        job.save()
        return redirect("viewjobPage")
    return render(request,"Recruiter/addjob.html")


def viewjobPage(request):
    user=request.user
    job=addjob_Model.objects.all()
    return render(request,"viewjob.html",{"job":job})

def deletePage(request,id):
    job=addjob_Model.objects.filter(id=id)
    job.delete()
    return redirect("viewjobPage")


def editPage(request,id):

    job=addjob_Model.objects.filter(id=id)
        
    return render(request,"Recruiter/edit.html",{"job":job})


def updatePage(request,id):
    user=request.user
    if request.method=="POST":
        jobTitle=request.POST.get("jobTitle")
        companyName=request.POST.get("companyName")
        description=request.POST.get("description")
        location=request.POST.get("location")

        job=addjob_Model(jobTitle=jobTitle,companyName=companyName,description=description,location=location,job_creator=user,update_at=user,id=id)
        job.save()
        return redirect("viewjobPage")