from django.db import models
from django.contrib import admin 
class vehicle_DB(models.Model):
    Name=models.CharField(max_length=10)
    Mobile=models.IntegerField()
    Address=models.TextField()
    No_Plate=models.CharField(primary_key=True)
    Email=models.EmailField()
    Vehicle_model=models.CharField()
    Damage_percentage=models.FloatField()
class vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["Name","Mobile","Address","No_Plate","Email","Vehicle_model","Damage_percentage"]
