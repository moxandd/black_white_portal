from rest_framework.serializers import ModelSerializer
from apps.core.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price')
