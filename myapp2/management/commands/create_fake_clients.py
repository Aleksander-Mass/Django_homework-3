from django.core.management.base import BaseCommand
from myapp2.models import Client


class Command(BaseCommand):
    help = "Generate fake clients"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count clients')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user = Client(name=f'Name{i}', email=f'mail{i}@mail.ru', phone='+79999999999',
                          address=f'127427, Москва, ул. Академика Королева, {i}')
            user.save()

