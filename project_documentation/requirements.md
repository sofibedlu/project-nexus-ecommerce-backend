# Project Nexus: E-Commerce Backend

## Overview
A robust backend system for e-commerce platforms handling:
- Product data management
- User authentication (JWT-based)
- Cart & order processing
- Payment handling
- Advanced API features (filtering, sorting, pagination)

Built with **Django** and **PostgreSQL**, focusing on scalability, performance, and security.

---

## Project Goals
1. **CRUD APIs** for users, products, categories, carts, orders, and payments
2. **Advanced API Features**
   - Filtering by category/attributes
   - Sorting by price/other fields
   - Pagination for large datasets
3. **Database Optimization**
   - PostgreSQL with strategic indexing
4. **User Authentication** via JWT
5. **Cart & Order Management** with status tracking
6. **Payment Handling** with transaction recording
7. **API Documentation** using Swagger/OpenAPI

---

## Requirements

### Functional Requirements
**User Management**
- Registration & Login with JWT
- Profile viewing/updating

**Category Management**
- CRUD operations
- Mandatory product associations

**Product Management**
- CRUD operations
- Filtering/Sorting/Pagination
- Attributes: name, description, price, category

**Cart Management**
- 1:1 user-cart relationship
- Add/update/remove items
- Cart content retrieval

**Order Management**
- Cart-to-order conversion
- Status tracking (pending → shipped → delivered)
- Multi-item order support

**Payment Handling**
- Payment method/status recording
- 1:1 order-payment linkage
- Status updates (completed/failed)

**API Documentation**
- Swagger/OpenAPI integration
- Request/response examples

### Non-Functional Requirements
- **Performance:** Optimized queries & caching
- **Scalability:** Horizontal/vertical scaling
- **Security:** HTTPS, input validation, secure storage
- **Maintainability:** Clean code & documentation
- **Deployment:** Docker & CI/CD readiness

---

## System Architecture
**Backend Framework:** Django  
**Database:** PostgreSQL (index-optimized)  
**Authentication:** JWT  
**API Docs:** Swagger/OpenAPI  

---

## Data Modeling
- **User:** `username`, `email`, `password`, timestamps (1:1 Cart, 1:Many Orders)
- **Category:** `name`, `description`, timestamps (1:Many Products)
- **Product:** `name`, `description`, `price`, timestamps (Many:1 Category)
- **Cart:** 1:1 User, 1:Many Cart Items
- **Cart Item:** `quantity`, links to Product & Cart
- **Order:** `status`, `total_amount`, `order_date` (1:Many Order Items)
- **Order Item:** `quantity`, `unit_price`, links to Product & Order
- **Payment:** `amount`, `method`, `status`, links to Order

---

## API Endpoints Overview

### Authentication
- `POST /api/auth/register` – User registration
- `POST /api/auth/login` – JWT generation

### Products
- `GET /api/products/` – Filtered/sorted/paginated list
- `POST /api/products/` – Create product
- `GET|PUT|DELETE /api/products/{id}/` – Retrieve/update/delete

### Categories
- `GET /api/categories/` – List categories
- `POST /api/categories/` – Create category
- `GET|PUT|DELETE /api/categories/{id}/` – Retrieve/update/delete

### Cart
- `GET /api/cart/` – Retrieve cart
- `POST /api/cart/items/` – Add item
- `PUT /api/cart/items/{item_id}/` – Update quantity
- `DELETE /api/cart/items/{item_id}/` – Remove item

### Orders
- `POST /api/orders/` – Create from cart
- `GET /api/orders/` – User's order history
- `GET|PUT|DELETE /api/orders/{id}/` – Retrieve/update/cancel

### Payments
- `POST /api/payments/` – Create payment
- `GET|PUT|DELETE /api/payments/{id}/` – Retrieve/update/cancel

---

## Development Roadmap
1. **Environment Setup**
   - Initialize Git repo
   - Configure Django + PostgreSQL

2. **Model & Authentication**
   - Implement all Django models
   - JWT authentication setup

3. **API Development**
   - CRUD endpoints
   - Filter/sort/paginate logic
   - Cart/order/payment workflows

4. **Documentation**
   - Swagger integration
   - Endpoint examples

5. **Optimization**
   - Database indexing
   - Query/caching improvements

6. **Deployment**
   - CI/CD pipeline
   - Staging/production setup

---

## Version Control Strategy
**Git Workflow**
- Feature branches (`feat/`, `fix/`, `docs/`)
- Conventional commit messages
- Pull requests + code reviews