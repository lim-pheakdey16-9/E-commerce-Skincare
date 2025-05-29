from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'accounts/index.html')

def dashboard(request):
    return render(request, 'accounts/admin/index.html')

def test(request):
    return render(request, 'accounts/admin/test.html')