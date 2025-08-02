'''
Created on 15 de jul. de 2025

@author: masterdev
'''

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
