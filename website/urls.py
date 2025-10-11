from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app1.urls')),  # root -> app1
    path('admin/', admin.site.urls),
]