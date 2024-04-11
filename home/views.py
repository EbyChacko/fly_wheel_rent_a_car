from django.shortcuts import render, redirect
from .forms import CustomerMessageForm

# Create your views here.

def index(request):
    """To return home page"""
    return render(request, 'home/index.html')

def contact(request):
    """To perform the messaging by the user to the hopital"""

    form = CustomerMessageForm()
    if request.method == 'POST':
        form = CustomerMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'home/contact.html', {
        'form': form,
    })


def about(request):
    """To return contact page"""
    return render(request, 'home/about.html')