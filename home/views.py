from django.shortcuts import render, redirect
from .forms import CustomerMessageForm

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
            return redirect('contact')
    return render(request, 'home/contact.html', {
        'form': form,
    })


def about(request):
    """To load about page"""
    return render(request, 'home/about.html')