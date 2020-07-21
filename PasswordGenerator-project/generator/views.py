from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    password_dict = {'password':'ihidguyuy'}
    return render(request, 'generator/home.html', password_dict)

def about(request):

    return render(request, 'generator/about.html')

def password(request):

    characters = 'abcdefghijklmnopqrstuvwxyz'

    if request.GET.get('uppercase'):
        Uppercase = characters.upper()
        characters = list(characters)
        characters.extend(list(Uppercase))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()?'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))

    password_dict = ''

    for x in range(length):
        password_dict += random.choice(characters) 

    return render(request, 'generator/password.html', {'password':password_dict})