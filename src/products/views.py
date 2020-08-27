from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.
def product_create_view(request):
    obj = Product.objects.get(id=5)
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form

    }
    return render(request, "product/ip_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=0)
    context = {
        'object':obj

    }
    return render(request, "product/detail.html" , context)