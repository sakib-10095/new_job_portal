from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER=[
        ("recruiter","Recruiter"),
        ("jobseeker","Jobseeker")
    ]

    display_name=models.CharField(max_length=120)
    email=models.EmailField(max_length=120)
    password=models.CharField(max_length=120)
    confirm_password=models.CharField(max_length=120)
    user_type=models.CharField(choices=USER,max_length=120)

    def __str__(self):
        return self.display_name
    
class addjob_Model(models.Model):
    jobTitle=models.CharField(max_length=250)
    companyName=models.CharField(max_length=120)
    description=models.TextField(null=True)
    location=models.CharField(max_length=120)
    job_creator=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    creat_at=models.TimeField(auto_now_add=True,null=True)
    update_at=models.TimeField(auto_now=True,null=True)

    def __str__(self):
        return self.jobTitle
