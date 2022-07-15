from django.db import models

# Create your models here.
class Event(models.Model):
    event_name=models.CharField(max_length=50)
    start_date=models.DateField
    start_time=models.TimeField
    finish_date=models.DateField
    finish_time=models.TimeField
    event_city=models.CharField(max_length=40)

class Info(models.Model):
    rollnum=models.CharField(max_length=15 , primary_key='true')
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    email=models.EmailField
    current_city=models.CharField(max_length=50)
    yog=models.CharField(max_length=10)
    contact=models.CharField(max_length=12)
    password=models.CharField(max_length=50)
    status=models.TextField(max_length=400)

class Stories(models.Model):
    story=models.TextField(max_length=1000)
    magzine=models.FileField
    insti_update=models.TextField(max_length=1000)
    gallery=models.ImageField
    achievements=models.TextField(max_length=1000)



