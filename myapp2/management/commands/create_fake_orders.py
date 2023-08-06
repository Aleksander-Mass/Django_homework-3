from django.core.management.base import BaseCommand
from myapp2.models import Order, Client, Product


class Command(BaseCommand):
    help = "Generate fake orders"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count orders')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        clients = Client.objects.all()
        products = Product.objects.all()
        count_clients = len(clients)
        count_products = len(products)
        for i in range(count):
            set_products = set([products[i % count_products], products[(i + 1) % count_products]])
            order = Order.objects.create(customer=clients[i % count_clients], total_price=2 * i)
            order.products.set(set_products)
            order.save()
