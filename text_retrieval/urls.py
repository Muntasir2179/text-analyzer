from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login_success/', views.login_success, name='login_success'),
    path('signup/', views.signup, name='signup'),
    path('save_signup_info/', views.save_signup_info, name='save_signup_info'),
    path('text_analyze/', views.text_analyze, name='text_analyze'),
    path('text_analyze/chat/', views.chat, name='chat'),
    path('response_history/', views.response_history, name='response_history'),
]