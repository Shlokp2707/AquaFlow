from django.shortcuts import render
from members.models import Member
from accounts.models import Myuser


def home_view(request):
    return render(request, 'Home.html')

def dashboard_view(request):
    user_id =request.session.get('user_id')
    member = Member.objects.filter(u_id_id=user_id).first()
    members =Member.objects.filter(u_id_id=user_id)
    print(member)

    context = {
        'members':members,
        'user_id': user_id,
        'first_name': request.session.get('first_name'),
        'is_active': member.is_active if member else False,
        'end_date': member.end_date if member else None,
    }
    # print(context)
    return render(request, 'dashboard.html',context)

def membership_view(request):
    return render(request, 'membership.html')

def dashboard(request):
    return render(request,dashboard)
def contact_us(request):
    return render(request,"contactus.html")