"""
URL configuration for hospedagemapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('client.urls', namespace='client')),
    path('hospedagens/', include('hosting.urls', namespace='hosting')),
    path('categorias/', include('category.urls', namespace='category')),
    path('reservas/', include('reservation.urls', namespace='reservation')),
    path('itens_reserva/', include('reservationhosting.urls', namespace='reservationhosting')),
    path('avaliacoes/', include('review.urls', namespace='review')),
    path('enderecos/', include('address.urls', namespace='address')),
]
