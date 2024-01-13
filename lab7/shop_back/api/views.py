from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Product

# Create your views here.
@require_http_methods(["GET"])
def get_active_products(request):
    active_products = Product.objects.filter(is_active=True, quantity__gt=0)
    products_data = [
        {
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'quantity': product.quantity,
            'category': product.category.name,
        }
        for product in active_products
    ]
    return JsonResponse({'products': products_data})
