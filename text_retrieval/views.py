from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def text_analyze(request):
    return render(request=request, template_name='text_analyze.html')

def chat(request):
    return render(request=request, template_name='chat.html')

def response_history(request):
    return render(request=request, template_name='table.html')