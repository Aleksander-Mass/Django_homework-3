from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='cookies', description='Американское печенье кукис с шоколадом', price=100, count=10)
        product.save()