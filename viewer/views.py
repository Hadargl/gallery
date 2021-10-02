from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def viewer_home(request):
    return render(request, 'viewer/home.html')

def viewer_gallery_1(request):
    return render(request, 'viewer/gallery1.html')
