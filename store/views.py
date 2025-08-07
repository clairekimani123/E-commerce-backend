from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartItemDeleteView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

# Update urls.py to include the delete endpoint
# In store/urls.py:
from django.urls import path
from .views import ProductListCreateView, CartItemListCreateView, CartItemDeleteView

urlpatterns = [
    path('api/products/', ProductListCreateView.as_view(), name='product-list'),
    path('api/cart-items/', CartItemListCreateView.as_view(), name='cart-item-list'),
    path('api/cart-items/<int:pk>/', CartItemDeleteView.as_view(), name='cart-item-delete'),
]