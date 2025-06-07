from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'hosting'

router = routers.DefaultRouter()
router.register('', views.HostingViewSet, basename='Hospedagens')

urlpatterns = [
    path('', include(router.urls))
]