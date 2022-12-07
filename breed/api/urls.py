from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('api/v1/breeds', views.BreedViewset, basename='breeds')

urlpatterns = router.urls
