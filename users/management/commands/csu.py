from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            phone='',
            avatar='',
            town='',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('PGNWyG')
        user.save()