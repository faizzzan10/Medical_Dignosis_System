from django.urls import path
from . import views
urlpatterns = [path('', views.home, name='home'), 
               path('register/', views.register_view, name='register'), path('login/', views.login_view, name='login'), path('logout/', views.logout_view, name='logout'), path('diagnosis/', views.diagnosis_home, name='diagnosis_home'), path('diagnosis/run-forward/', views.run_forward, name='run_forward'), path('diagnosis/backward-wizard/', views.backward_wizard, name='backward_wizard')]
