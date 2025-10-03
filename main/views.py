from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def application(request):
    return render(request, 'application.html')

def login_view(request):
    return render(request, 'login.html')

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')
