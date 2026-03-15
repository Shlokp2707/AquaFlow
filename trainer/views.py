from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Trainer
from members.models import Member 

def trainer_login_view(request):
    if request.method=='POST':
        email =request.POST.get('email')
        password =request.POST.get('password')
        trainer =Trainer.objects.filter(email =email,password =password).first()
        if trainer is not None:
            request.session['trainer_id'] = trainer.t_id
            request.session['first_name'] = trainer.first_name
            print("successfully loged in")
            return redirect("trainer_dashboard")
        else: 
            print("login failed")
            messages.error(request,"invalid credentials")
            return redirect("trainer_login")
    return render(request,'trainer_login.html')
def trainer_dashboard_view(request):
    trainer =Trainer.objects.filter(t_id =request.session.get('trainer_id')).first()
    members =Member.objects.filter(time_slot=trainer.time_slot)
    print(members) 
    context ={
         'id' :trainer.t_id,
         'first_name':trainer.first_name,
         'members':members
    }        
  
    return render(request,"trainer_dashboard.html",context)
def trainer_profile_view(request): 
    trainer =Trainer.objects.filter(t_id =request.session.get('trainer_id')).first()
    if not trainer:
        return redirect("trainer_login")
    context= {
            'first_name':trainer.first_name,
            'last_name':trainer.Last_name,
            'email':trainer.email
        }
        
    if request.method =='POST':
            trainer.first_name =request.POST.get("first_name")
            trainer.Last_name =request.POST.get("Last_name")
            trainer.dob =request.POST.get("dob")
            trainer.gender =request.POST.get("gender")
            trainer.experience =request.POST.get("experience")
            trainer.speciality =request.POST.get("speciality")
            trainer.time_slot =request.POST.get("time_slot")
            trainer.phone_number =request.POST.get("phone_number")
            trainer.adhaar_no =request.POST.get("adhaar_no")
            trainer.address =request.POST.get("address")
            trainer.save()
            print(trainer)
            return redirect("trainer_dashboard")
    return render(request,"trainer_profile.html",context)
