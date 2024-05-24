
from django.urls import path, include
from .views import index, paquetes

urlpatterns = [
    path('',index,name='index'),
    path('paquetes/',paquetes, name='paquetes'),
 
]