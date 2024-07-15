from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.core.models import Product
from apps.core.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer