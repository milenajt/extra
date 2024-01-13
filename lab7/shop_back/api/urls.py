from django.urls import path
from .views import get_active_products

urlpatterns = [
    path('products/', get_active_products, name='get_active_products'),
]
