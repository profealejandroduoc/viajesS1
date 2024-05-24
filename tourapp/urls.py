
from django.urls import path, include
from .views import index, paquetes, productos

urlpatterns = [
    path('',index,name='index'),
    path('paquetes/',paquetes, name='paquetes'),
    path('productos/',productos,name='productos'),
 
]