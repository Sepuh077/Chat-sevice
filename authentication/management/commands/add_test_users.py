from django.core.management.base import BaseCommand
from authentication.models import Profile
import random, string
from django.utils.timezone import now


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(10):
            try:
                Profile.objects.create(
                    email=f'test{i}@gmail.com',
                    name=''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 11))) + " " + ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 11))) + " " + ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 11))),
                    birth_date=now().date(),
                    password='test'
                )
            except Exception as exc:
                print(exc)
