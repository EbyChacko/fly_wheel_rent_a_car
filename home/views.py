from django.shortcuts import render, redirect
from .forms import CustomerMessageForm
from django.contrib import messages

# Create your views here.

def index(request):
    """To load home page"""
    return render(request, 'home/index.html')

def contact(request):
    """To perform the messaging by the user to the fly wheel"""

    form = CustomerMessageForm()
    if request.method == 'POST':
        form = CustomerMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Message has been send successfully. We will contact you soon!')
            return redirect('/')
    return render(request, 'home/contact.html', {
        'form': form,
    })


def about(request):
    """To load about page"""
    return render(request, 'home/about.html')

def login_or_signup(request):
    """To load login_or_signup page"""
    return render(request, 'home/login_or_signup.html')