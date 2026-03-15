from django.db import models

class Myuser(models.Model):
    gender_choices =[
        ('male','Male'),
        ('female','Female')
    ]
    u_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128,)
    dob = models.DateField(null=True,blank=True,default ="2000-01-01")
    gender = models.CharField(max_length=6, choices=gender_choices,null=True, blank=True)
    address = models.TextField(max_length=300,null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True,null=True, blank=True)
    adhaar_no = models.CharField(max_length=12, unique=True,null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"