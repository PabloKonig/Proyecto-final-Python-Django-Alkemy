from django.urls import path
from .views import primera_prueba

app_name = 'compra'

urlpatterns = [
    path("inicio/", primera_prueba, name='primera_prueba'),
]
