import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create demo user and optional superuser from env vars on deploy'

    def handle(self, *args, **options):
        User = get_user_model()

        # Always ensure the demo user exists with the correct password
        demo, created = User.objects.get_or_create(username='demo', defaults={'email': 'demo@demo.com'})
        demo.set_password('demo1234')
        demo.save()
        if created:
            self.stdout.write('Demo user created.')
        else:
            self.stdout.write('Demo user password reset.')

        # Create superuser from env vars if one doesn't exist yet
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')

        if not username or not password:
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(f'Superuser "{username}" already exists — skipping.')
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(f'Superuser "{username}" created successfully.')
