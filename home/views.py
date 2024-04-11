from django.shortcuts import render

# Create your views here.

def index(request):
    """To return home page"""
    return render(request, 'home/index.html')

def contact(request):
    """To return contact page"""
    return render(request, 'home/contact.html')

def about(request):
    """To return contact page"""
    return render(request, 'home/about.html')