from django.db import models
from accounts.models import Myuser
class Member(models.Model):
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
    plan_choices=[
        ('basic','2000'),
        ('priminum','3000'),
        ('elite','5000'),
        ('family','6000')
    ]
    m_id =models.AutoField(primary_key=True)
    u_id=models.ForeignKey(Myuser,on_delete = models.CASCADE,null =True,blank =True)
    first_name =models.CharField(max_length=50)
    Last_name =models.CharField(max_length=50)
    dob =models.DateField(default ="2000-01-01")
    gender =models.CharField(max_length=6,choices=gender_choices)
    time_slot=models.CharField(max_length=10,choices=time_slot_choices)
    plan =models.CharField(max_length =10,choices=plan_choices,default ='basic')
    start_data =models.DateField(auto_now=True)
    end_date =models.DateField(null =True,blank=True)
    is_active =models.BooleanField(default =False)
    def __str__(self):
        return f"{self.first_name}"