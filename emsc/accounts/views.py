from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home_page')


def contactUs(request):
    return render(request, 'accounts/ContactUs.html')