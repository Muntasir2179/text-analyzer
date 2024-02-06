from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return render(request, 'index.html')

@login_required(login_url='login')
def text_analyze(request):
    return render(request=request, template_name='text_analyze.html')

@login_required(login_url='login')
def chat(request):
    return render(request=request, template_name='chat.html')

@login_required(login_url='login')
def response_history(request):
    return render(request=request, template_name='table.html')

def login_function(request):
    if request.method == 'GET':
        print("inside login GET")
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request=request, template_name='login.html', context=context)

    else:
        print("inside login POST")
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            print(username)
            print(password)

            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('index')
        else:
            context = {
                "form": form
            }
            return render(request=request, template_name='login.html', context=context)

def signup_function(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request=request, template_name='signup.html', context=context)
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        context = {
            'form': form
        }
        
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request=request, template_name='signup.html', context=context)
        
def logout_function(request):
    logout(request=request)
    return redirect('login')