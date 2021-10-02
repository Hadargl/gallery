from django.shortcuts import render
from django.http import HttpResponse

def viewer_home(request):
    return render(request, 'viewer/home.html')
