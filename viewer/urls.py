from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewer_home, name='viewer-home'),
    path('gallery1/', views.viewer_gallery_1, name='gallery-1'),
]

