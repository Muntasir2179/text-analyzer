from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from dashboard.settings import BASE_DIR
import os

from .embedding_model import VectorDatabase


# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request=request, template_name='index.html', context={'current_user': request.user})

@login_required(login_url='login')
def text_analyze(request):
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('files')
        for uploaded_file in uploaded_files:
            if uploaded_file.content_type == 'text/plain':  # Check if the file is a text file
                # Save the file to the 'uploads/' folder
                with open(f'uploads/{uploaded_file.name}', 'wb') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
                destination.close()
            
        return render(request=request, template_name='chat.html', context={'current_user': request.user})
    else:
        return render(request=request, template_name='text_analyze.html', context={'current_user': request.user})

@login_required(login_url='login')
def chat(request):
    return render(request=request, template_name='chat.html', context={'current_user': request.user})

@login_required(login_url='login')
def response_history(request):
    return render(request=request, template_name='table.html', context={'current_user': request.user})

def login_function(request):
    if request.method == 'GET':
        # if authenticated user tries to access the login url again then redirect to home page
        if request.user.is_authenticated:
            return redirect('index')
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request=request, template_name='login.html', context=context)

    else:
        error_message = None
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('index')
        else:
            username = request.POST.get('username')
            all_user = User.objects.all()
            error_message = "No user exit with this username"
            for single_user in all_user:
                if username == single_user.username:
                    error_message = "Password doesn't match"

            context = {
                "form": form,
                "error_message": error_message
            }
            return render(request=request, template_name='login.html', context=context)

def signup_function(request):
    if request.method == 'GET':
        # if authenticated user tries to access the signup url again then redirect to home page
        if request.user.is_authenticated:
            return redirect('index')
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request=request, template_name='signup.html', context=context)
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # forming error messages
        error_messages = check_user_credentials({
            'username': request.POST.get('username'),
            'password1': request.POST.get('password1'),
            'password2': request.POST.get('password2')
        })
        context = {
                'form': form,
                'error_messages': error_messages
        }
        if len(error_messages.keys()) == 0:
            if form.is_valid():
                user = form.save()
                if user is not None:
                    return redirect('login')
        else:
            return render(request=request, template_name='signup.html', context=context)
        
def logout_function(request):
    # listing all the files in 'uploads' folder and deleting those uploaded files
    file_list = os.listdir(BASE_DIR / 'uploads')
    if len(file_list) != 0:
        for file_name in file_list:
            os.remove(os.path.join(BASE_DIR / 'uploads', file_name))
    logout(request=request)
    return redirect('login')


def check_user_credentials(user_info):
    username = user_info['username']
    password1 = user_info['password1']
    password2 = user_info['password2']

    all_user = User.objects.all()
    error_messages = {}
    for single_user in all_user:
        if username == single_user.username:
            error_messages['username_error_msg'] = "Username is taken"

    if password1 != password2:
        error_messages['password_error_msg'] = "Password doesn't match"
    else:
        if len(password1) < 8:
            error_messages['password_error_msg'] = "Minimum password length is 8"
    
    return error_messages