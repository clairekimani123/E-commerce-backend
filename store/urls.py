from django.urls import path
from .views import ProductListCreateView, CartItemListCreateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('cart/', CartItemListCreateView.as_view(), name='cart-list-create'),
]
