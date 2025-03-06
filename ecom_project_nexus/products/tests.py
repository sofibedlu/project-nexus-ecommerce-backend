# Python
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User
from .models import Product, Category
from decimal import Decimal
from django.core.cache import cache

class ComprehensiveAPITests(APITestCase):
    def setUp(self):
        # URLs from the apps
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.token_refresh_url = reverse('token_refresh')
        # Router auto-names product-list and category-list are used
        self.product_list_url = reverse('product-list')
        self.category_list_url = reverse('category-list')
        
        # Create an admin user via registration endpoint, then update role/staff
        admin_data = {
            "email": "admin@example.com",
            "first_name": "Admin",
            "last_name": "User",
            "password": "strongadminpass",
            "role": "admin"
        }
        self.client.post(self.register_url, admin_data, format="json")
        self.admin_user = User.objects.get(email="admin@example.com")
        self.admin_user.role = "admin"
        self.admin_user.is_staff = True
        self.admin_user.save()
        
        # Register a regular user
        regular_data = {
            "email": "user@example.com",
            "first_name": "Regular",
            "last_name": "User",
            "password": "stronguserpass",
            "role": "user"
        }
        self.client.post(self.register_url, regular_data, format="json")
        
        # Login as admin and regular user to obtain JWT tokens.
        admin_login = self.client.post(self.login_url, {"email": "admin@example.com", "password": "strongadminpass"}, format="json")
        self.admin_token = admin_login.data['access']
        user_login = self.client.post(self.login_url, {"email": "user@example.com", "password": "stronguserpass"}, format="json")
        self.regular_token = user_login.data['access']
        
        # Use admin token to create a sample category.
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        category_data = {"name": "Electronics", "description": "Electronic items"}
        category_resp = self.client.post(self.category_list_url, category_data, format="json")
        self.assertEqual(category_resp.status_code, status.HTTP_201_CREATED)
        self.category_id = category_resp.data['catagory_id']
        self.client.credentials()
    
    def test_registration_and_login(self):
        # Tokens already set in setUp; verify they are not empty.
        self.assertIsNotNone(self.admin_token)
        self.assertIsNotNone(self.regular_token)
     
    def test_product_list_access(self):
        response = self.client.get(self.product_list_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_product_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        product_data = {
            "name": "Laptop",
            "description": "A powerful laptop.",
            "price": "1299.99",
            "category_id": self.category_id  # write-only field for assigning category
        }
        response = self.client.post(self.product_list_url, product_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.credentials()
        
    def test_create_product_as_regular_user_forbidden(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.regular_token)
        product_data = {
            "name": "Smartphone",
            "description": "Latest smartphone.",
            "price": "699.99",
            "category_id": self.category_id
        }
        response = self.client.post(self.product_list_url, product_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.credentials()
        
    def test_filter_products_by_category(self):
        # Create a product using admin credentials.
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        product_data = {
            "name": "Tablet",
            "description": "A lightweight tablet.",
            "price": "499.99",
            "category_id": self.category_id
        }
        self.client.post(self.product_list_url, product_data, format="json")
        self.client.credentials()
        
        # Filter products by category primary key.
        response = self.client.get(self.product_list_url, {'category': self.category_id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for product in response.data.get('results', []):
            self.assertEqual(product['category']['catagory_id'], self.category_id)
        
    def test_sort_and_pagination_products(self):
        # Create multiple products for testing pagination and ordering.
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        for i in range(15):
            product_data = {
                "name": f"Product {i}",
                "description": f"Description {i}",
                "price": str(50 + i),
                "category_id": self.category_id
            }
            self.client.post(self.product_list_url, product_data, format="json")
        self.client.credentials()
        
        # Test pagination (assuming DRF pagination is configured).
        response = self.client.get(self.product_list_url, {'page': 2}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        
        # Test sorting by price in descending order.
        response = self.client.get(self.product_list_url, {'ordering': '-price'}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        prices = [Decimal(prod['price']) for prod in response.data.get('results', [])]
        self.assertEqual(prices, sorted(prices, reverse=True))
        
    def test_duplicate_category_creation(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        duplicate_data = {"name": "Electronics", "description": "Duplicate category"}
        response = self.client.post(self.category_list_url, duplicate_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("already exists", str(response.data))
        self.client.credentials()

    def test_caching_of_product_list(self):
        # Clear cache to start with a clean slate.
        cache.clear()
        
        # Get the product list endpoint response
        response1 = self.client.get(self.product_list_url, format="json")
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        
        # Create a new product using admin credentials
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        product_data = {
            "name": "New Cached Product",
            "description": "Should not appear until cache expires",
            "price": "100.00",
            "category_id": self.category_id
        }
        create_resp = self.client.post(self.product_list_url, product_data, format="json")
        self.assertEqual(create_resp.status_code, status.HTTP_201_CREATED)
        self.client.credentials()
        
        # Immediately fetch the product list again.
        response2 = self.client.get(self.product_list_url, format="json")
        # The cached response should be identical to response1 (i.e. not contain the new product).
        self.assertEqual(response1.data, response2.data)
        
        # Clear cache manually and fetch again.
        cache.clear()
        response3 = self.client.get(self.product_list_url, format="json")
        # Now the new product should be visible.
        self.assertNotEqual(response2.data, response3.data)
        
    def test_token_refresh(self):
        # Retrieve refresh token from a login.
        login_resp = self.client.post(self.login_url, {"email": "user@example.com", "password": "stronguserpass"}, format="json")
        refresh_token = login_resp.data.get('refresh')
        response = self.client.post(self.token_refresh_url, {"refresh": refresh_token}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)