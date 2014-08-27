from django.shortcuts import render
from data.models import *

def home(request):
    return render(request,'index.html')