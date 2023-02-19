from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    yourpassword = ''
    chars = list('abcdefghijklmnopqrstwxyz')
    lenght = int(request.GET.get('lenght'))
    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*_+№%:;?/'))
    for x in range(lenght):
            yourpassword += random.choice(chars)
    return render(request,'generator/password.html',{'password':yourpassword})
def info(request):
    return render(request,'generator/information.html')
