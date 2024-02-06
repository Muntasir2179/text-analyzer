from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('text_analyze/', views.text_analyze, name='text_analyze'),
    path('text_analyze/chat/', views.chat, name='chat'),
    path('response_history/', views.response_history, name='response_history'),
]