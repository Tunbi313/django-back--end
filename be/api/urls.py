# api/urls.py

from django.urls import path
from .views import RegisterView, LoginView
from .product import manage_product
from .cart import cart_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('product/', manage_product, name='manage_product'),  # POST cho thêm sản phẩm
    path('product/<int:product_id>/', manage_product, name='manage_product_by_id'),  # PUT, DELETE cho sửa/xóa sản phẩm
    path('cart/', cart_view, name='cart_view'),  # GET, POST cho giỏ hàng
]
