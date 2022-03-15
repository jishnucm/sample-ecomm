from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request,'ecomm/index.html')

def signup(request):
    return render(request,'ecomm/index1.html')
