from django.core.management.base import BaseCommand
from decimal import Decimal
from products.models import Category, Product

class Command(BaseCommand):
    help = 'Seeds the database with sample categories and products.'

    def handle(self, *args, **options):
        # Remove existing data
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Create categories
        electronics = Category.objects.create(name='Electronics', description='Electronic items.')
        clothing = Category.objects.create(name='Clothing', description='Apparels and garments.')

        # Create products
        Product.objects.create(
            name='Smartphone',
            description='Latest smartphone with high performance',
            price=Decimal('699.99'),
            category=electronics
        )
        Product.objects.create(
            name='Laptop',
            description='High performance laptop built for professionals',
            price=Decimal('1299.99'),
            category=electronics
        )
        Product.objects.create(
            name='T-Shirt',
            description='Comfortable cotton T-Shirt',
            price=Decimal('19.99'),
            category=clothing
        )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))