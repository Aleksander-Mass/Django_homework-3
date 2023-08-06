from django.shortcuts import render, get_object_or_404
from myapp2.models import Client, Order, Product
from datetime import datetime, timedelta


def client_products(request, client_id, days):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client, date_ordered__gte=datetime.now() - timedelta(days=days))
    products = []
    for order in orders:
        products.extend([i.name for i in order.products.all()])

    context = {'client': client, 'days': days, 'products': set(products)}
    return render(request, 'myapp2/client_products.html', context)