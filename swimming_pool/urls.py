from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name ='home'),
    path('dashboard/',dashboard_view,name='dashboard'),
    path('membership/',membership_view,name='membership'),
    path("contactus/",contact_us,name ="contactus"),
    path('accounts/', include('accounts.urls')),
    path('member/',include("members.urls")),
    path('trainer/',include("trainer.urls"))

]