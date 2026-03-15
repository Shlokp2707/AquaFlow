from django.shortcuts import render
from .models import Myuser
from django.contrib import messages
from django.shortcuts import redirect

def signout_view(request):
    return render (request,'signout.html')   
def login_view(request):
    if request.method == 'POST':
        email =request.POST['email']
        password =request.POST['password']
        try:
            user = Myuser.objects.get(email=email, password=password)
            if user is not None:
                session = request.session
                session['user_id'] = user.u_id
                session['first_name'] = user.first_name
                print("Login Successful")   
                return redirect('dashboard')
        except Myuser.DoesNotExist:
            print('login failed')
            messages.warning(request,'Invalid credentials')
            return redirect('login')
     
    return render(request,'login.html')

def signup_view(request):
    if request.method =='POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name'] 
        password = request.POST['password'] 
        confirm_password =request.POST['confirm_password']

        if Myuser.objects.filter(email=email).exists():
            return render(request,'signup.html',{'error':'Email already exists'}) 
        if password !=confirm_password:
            return render(request,'signup.html',{'error':'Passwords do not match'})
        
        my_user =Myuser.objects.create(email=email,first_name=first_name,last_name=last_name,password=password)
        my_user.save() 
        print("signup Successful")
        messages.success(request,'Account has been created successfully')
        return redirect('login')
    return render(request, 'signup.html')
  

def profile_view(request):
    user = Myuser.objects.filter(u_id=request.session.get('user_id')).first()
    context ={
        'first_name':user.first_name,
        'last_name':user.last_name,
        'email':user.email
    }
    # print(context)
    if request.method =='POST':
        if  Myuser.objects.filter(adhaar_no=request.POST.get('adhaar_no')).exists():
                messages.error(request, 'Adhaar number is already registered. Use a different one.')
                return redirect('profile')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.phone_number =request.POST.get('mobile_no')   
        user.address =request.POST.get('address')
        user.dob =request.POST.get('dob')
        user.gender =request.POST.get('gender')
        user.adhaar_no =request.POST.get('adhaar_no')
        user.save()
        print(user) 
        return redirect('dashboard')
    return render(  request,'profile.html',context)
        