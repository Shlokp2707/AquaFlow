from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Member
from accounts.models import Myuser
from datetime import date,datetime
def member_register_view(request):
    plan =request.GET.get('plan') 
    # print("Selected Plan:",plan)
    if request.method=='POST':
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        dob_str =request.POST.get('dob') 
        gender =request.POST.get('gender')
        time_slot =request.POST.get('time_slot')
        if plan is None:
            plan =request.POST.get('plan') 
        # print('request',request.POST.get)
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if int(age) < 5:
            messages.error(request, 'Age must be at least 5 years')
            return redirect('member_register')

        user =Myuser.objects.get(u_id =request.session.get('user_id'))
        member =Member(
            u_id =user,
            first_name=first_name,
            Last_name=last_name,
            dob=dob,
            gender=gender,
            plan=plan,  
            time_slot =time_slot,
            start_data =timezone.now(),
            end_date =timezone.now()+timezone.timedelta(days=30),
            is_active =True,
            )
        member.save()
        messages.success(request, 'Membership registration successful!')
        return redirect('dashboard')  
    return render(request,'mem_register.html',{'plan':plan})
def pass_view(request,member_id):
    member =Member.objects.get(m_id=member_id)
    user =Myuser.objects.get(u_id =member.u_id_id)
    context={
        "name":member.first_name + " " + member.Last_name,
        "gender": member.gender,
        "valid_upto":member.end_date,
        "address":user.address ,
        "phoneno": user.phone_number,
        "id":member.m_id,
        "plan": member.plan
    }
  
    return render(request,"pass.html",context =context)