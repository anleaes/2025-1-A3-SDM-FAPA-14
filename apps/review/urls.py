from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'review'

router = routers.DefaultRouter()
router.register('', views.ReviewViewSet, basename='avaliacoes')

urlpatterns = [
    path('', include(router.urls))
]