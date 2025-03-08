# Project Nexus: E-Commerce Backend

Project Nexus is a robust Django-based backend designed for e-commerce platforms. It handles product management, user authentication with JWT, category management, cart/order processing, and advanced API features like filtering, sorting, and pagination.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Architecture & Design](#architecture--design)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Documentation](#documentation)
- [Deployment](#deployment)

## Overview

Project Nexus provides a scalable backend solution with the following core functionalities:
- **User Management:** Secure registration and JWT-based authentication
- **Product & Category Management:** CRUD operations with filtering/sorting
- **Cart & Order Processing:** Complete purchase workflow management
- **Payment Handling:** Payment status tracking and recording
- **Caching:** Optimized endpoints via caching decorators
- **API Documentation:** Integrated Swagger/OpenAPI for self-documented APIs

## Features

- **User Authentication**  
  JWT-based registration/login system ([accounts/views.py](accounts/views.py))

- **Product Catalog**  
  Full CRUD operations for products and categories ([products/views.py](products/views.py))

- **Shopping Cart**  
  Add/update/remove items from user carts

- **Order Management**  
  Convert carts to orders with status tracking

- **Advanced API**  
  Filtering, sorting, pagination, and caching

- **Database Seeding**  
  Populate sample data via seed command ([products/management/commands/seed.py](products/management/commands/seed.py))

## Requirements

- Python 3.8+
- Django 4.2+
- PostgreSQL
- redis server
- python-environ

## Architecture & Design

Key architectural components:
- **Custom User Model:** Extended with role-based permissions ([accounts/models.py](accounts/models.py))
- **RESTful API:** Built using Django REST Framework
- **JWT Authentication:** Secure endpoints with refresh tokens ([accounts/serializers.py](accounts/serializers.py))
- **Caching:** Redis-based caching for high-traffic endpoints
- **PostgreSQL:** Primary database for relational data management

For detailed diagrams, see:
- [ERD Documentation](project_documentation/ERD/README.md)
- [Use Case Diagrams](project_documentation/use-case-diagrams/README.md)

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd ecom_project_nexus
2. **Create virtual environment:**
    ```python
    python3 -m venv env
    source env/bin/activate  # Linux/macOS
3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
4. **Configure environment:**
    - Create .env from .env.example
    - Set required values:
        ```ini
        SECRET_KEY=<your_key>
        DEBUG=True
        DB_NAME=<name>
        DB_USER=<user>
        DB_PASSWORD=<password>
        DB_HOST=<host>
        DB_PORT=<port>
## Configuration
Update ecom_project_nexus/settings.py as needed:
- **Database:** PostgreSQL configuration in DATABASES
- **Caching:** Redis settings for django_redis
- **JWT:** Token lifetimes in SIMPLE_JWT

## Running the Project
1. **Apply migrations:**
    ```sh
    python manage.py migrate
2. **Seed database (optional):**
    ```sh
    python manage.py seed
3. **Create superuser:**
    ```sh
    python manage.py createsuperuser
4. **Start server:**
    ```sh
    python manage.py runserver
- Access API documentation at /swagger/ or /redoc/

## API Endpoints

| Category       | Endpoint               | Methods          | Description                          |
|----------------|------------------------|------------------|--------------------------------------|
| Authentication | `/auth/register/`      | POST             | User registration                   |
| Authentication | `/auth/token/`         | POST             | Obtain JWT token                    |
| Products       | `/api/products/`       | GET, POST        | List/create products                |
| Products       | `/api/products/{id}/`  | GET, PUT, DEL    | Product details/update/delete       |
| Categories     | `/api/categories/`     | GET, POST        | List/create categories              |
| Carts          | `/api/cart/`           | GET, POST        | Manage shopping cart                |
| Orders         | `/api/orders/`         | GET, POST        | Order management                    |

## Testing

- Run comprehensive test suite:
    ```python
    python manage.py test

- **Tests cover:**
    - User registration/login
    - Product CRUD operations
    - API filtering/pagination
    - JWT token refresh
    - Caching mechanisms

## Documentation
Additional resources in project_documentation:
- Requirements
- Flowcharts
- User Stories
- ERD Diagrams

## Deployment
For production deployment:
- Use Docker containerization
- Configure CI/CD pipelines
- Set DEBUG=False in production
- Refer to deployment documentation for detailed instructions
