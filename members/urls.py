from django.urls import path
from .views import member_register_view,pass_view
urlpatterns = [
    path('',member_register_view, name='member_register'),
    path("pass/<int:member_id>/",pass_view,name='pass')
]