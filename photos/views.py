from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def links(request):
    return render(request, 'links.html')


def gallery(request):
    return render(request, 'gallery.html')


def add(request):
    if not request.user.is_authenticated:
        return redirect('index')

    return render(request, 'add.html')

# Create your views here.
