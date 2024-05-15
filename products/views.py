from django.shortcuts import render

from products.models import Product


def index(request):
    return render(request, 'products.html')

def products_id(request, product_id):
    product = Product.objects.get(pk=product_id)
    # Passa o produto como contexto para o template
    context = {}
    context['product'] = product
    # ou {'product': product} passado no 3° parâmetro abaixo:
    return render(request, 'productsId.html', context)