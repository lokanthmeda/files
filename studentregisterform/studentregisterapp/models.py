from django.db import models
class Collegedata(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    dob=models.DateField(max_length=100)
    email=models.EmailField(max_length=100)
    Father_name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    Mother_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

