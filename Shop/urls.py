from django.urls import path
from Shop import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('employee_login/', views.employee_login, name='employee_login'),
    path('checkout/', views.checkout, name='checkout'),
]   
