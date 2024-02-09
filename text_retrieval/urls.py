from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_function, name='login'),
    path('signup/', views.signup_function, name='signup'),
    path('logout/', views.logout_function, name='logout'),
    path('text_analyze/', views.text_analyze, name='text_analyze'),
    path('text_analyze/chat/', views.chat, name='chat'),
]