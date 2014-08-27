from django.shortcuts import render
from data.models import *

def home(request):
    items = UeberstellungZielgebiet.objects.all()
    return render(request,'index.html',{'items': items})