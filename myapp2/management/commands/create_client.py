from django.core.management.base import BaseCommand
from myapp2.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        user = Client(name='John', email='john@example.com',
                    phone='+79008007766', address='127427, Москва, ул. Академика Королева, 12')
        user.save()
