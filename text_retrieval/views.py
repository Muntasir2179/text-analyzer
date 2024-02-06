from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login_page')
def index(request):
    return render(request, 'index.html')

def text_analyze(request):
    return render(request=request, template_name='text_analyze.html')

def chat(request):
    return render(request=request, template_name='chat.html')

def response_history(request):
    return render(request=request, template_name='table.html')

def login(request):
    return render(request=request, template_name='login.html')

def signup(request):
    return render(request=request, template_name='signup.html')

def save_signup_info(request):
    return redirect('login')

def login_success(request):
    return redirect('index')