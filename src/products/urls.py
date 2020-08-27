from django.urls import path
from .views import product_detail_view,product_create_view

app_name = 'products'

urlpatterns = [
path('product/', product_detail_view, name='product'),
path('create/', product_create_view, name='create'),
    ]