from django.contrib import admin
from myapp.models import *


class CustomUser_Display(admin.ModelAdmin):
    list_display=("display_name","email","user_type")



admin.site.register(CustomUser,CustomUser_Display)
admin.site.register(addjob_Model)
