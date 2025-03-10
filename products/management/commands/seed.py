# Python
from django.core.management.base import BaseCommand
from products.models import Product, Category
import random
from faker import Faker

class Command(BaseCommand):
    help = 'Seed the database with categories and a variety of products.'

    def handle(self, *args, **options):
        fake = Faker()

        # Create categories
        category_names = ['Electronics', 'Clothing', 'Home', 'Books', 'Toys']
        categories = []
        for name in category_names:
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={'description': fake.text(max_nb_chars=100)}
            )
            categories.append(category)
            self.stdout.write(self.style.SUCCESS(f'Category "{name}" created.'))

        # Create multiple products with varying attributes
        num_products = 50  # Adjust number as needed for testing
        for i in range(num_products):
            product = Product.objects.create(
                name=fake.catch_phrase(),
                description=fake.text(max_nb_chars=200),
                price=round(random.uniform(10, 1000), 2),
                category=random.choice(categories)
            )
            self.stdout.write(self.style.SUCCESS(f'Product "{product.name}" created.'))

        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully.'))