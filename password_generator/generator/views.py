from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':"testingthis"})

def password(request):

    alphabet_string = string.ascii_lowercase
    chars = list(alphabet_string)

    if request.GET.get('uppercase'):
        chars.extend(list(string.ascii_uppercase))

    if request.GET.get("special"):
        chars.extend(list("!@#$%^&*()"))

    if request.GET.get("numbers"):
        chars.extend(list("0123456789"))

    length = int(request.GET.get('length', 12))

    the_password = ''

    for x in range(length):
        the_password += random.choice(chars)


    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')