from rest_framework import serializers
from .models import Product, CartItem

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.URLField(source='image_url')
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'image_url']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']
