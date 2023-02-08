from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    price = serializers.DecimalField(decimal_places=2, max_digits=7)
    description = serializers.CharField(max_length=200)
    info = serializers.CharField(max_length=200)
    digital = serializers.BooleanField(default=False)

    class Meta:
        model = Product












