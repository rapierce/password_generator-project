from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    the_Password = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special_Char'):
        characters.extend(list('~!@#$%^&*+='))

    length_Password = int(request.GET.get('length', 12))


    the_Password = ''
    for x in range(length_Password):
        the_Password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_Password})

def about(request):
    return render(request, 'generator/about.html')