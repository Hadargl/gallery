from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewer/', include('viewer.urls')),
    path('', include('viewer.urls')),
]
