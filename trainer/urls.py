
from django.urls import path
from .views import *
urlpatterns = [
  path('login/', trainer_login_view, name='trainer_login'),
  path('trainer_dashboard/', trainer_dashboard_view, name='trainer_dashboard'),
  path('trainer_profile/', trainer_profile_view, name='trainer_profile')  
]