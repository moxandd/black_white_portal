from rest_framework.routers import DefaultRouter
from apps.api.views import ProductViewSet
from django.urls import path


router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = []


urlpatterns += router.urls