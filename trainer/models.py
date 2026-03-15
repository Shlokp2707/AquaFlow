from django.db import models
class Trainer(models.Model):
    gender_choices =[
        ('male','Male'),
        ('female','Female')
    ]
    time_slot_choices =[
        ('slot1','6AM - 8AM'),
        ('slot2','8AM - 10AM'), 
        ('slot3','4PM - 6PM'),
        ('slot4','6PM - 8PM')
    ]
    speciality_choices =[
        ('beginer','Beginer Trainer'),
        ('intermediate','Intermediate Trainer'),
        ('professional','Professional Trainer'),
        ('liveguard','Lifeguard Trainer'),
        ('diver','Diver Trainer')]
    t_id =models.AutoField(primary_key=True)
    first_name =models.CharField(max_length=50)
    Last_name =models.CharField(max_length=50)
    email =models.EmailField(max_length=100,null =True,blank=True)
    dob =models.DateField(null=True,blank=True,default ="2000-01-01")
    password =models.CharField(max_length=128,default=123)
    gender =models.CharField(max_length=6,choices=gender_choices)
    experience =models.IntegerField(null=True,blank=True)
    speciality=models.CharField(max_length=15,choices=speciality_choices,null=True,blank=True)
    time_slot=models.CharField(max_length=10,choices=time_slot_choices)
    address =models.TextField(max_length=300,null=True,blank=True)
    phone_number =models.CharField(max_length=10)
    adhaar_no =models.CharField(max_length=12,unique=True,null=True,blank=True)
    def __str__(self):
        return f"{self.first_name}"
    