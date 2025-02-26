# Entity Relationship Diagram (ERD)

This folder contains the Entity Relationship Diagram (ERD) for the **Project Nexus E-Commerce Backend**. The diagram illustrates the relationships between system entities and outlines the database structure supporting core functionalities:
- User management
- Product catalog
- Cart management
- Order processing
- Payment handling

> **Note:** The ERD image is generated from a Mermaid diagram included in the repository. **Always update both the Mermaid code and image** when making schema changes to maintain consistency.

---

## Entities

### User
- **Table Name:** `USER`
- **Primary Key:** `id`
- **Fields:**
  - `username`: Unique login identifier
  - `email`: Communication/authentication address
  - `password`: Encrypted authentication
  - `created_at`: Account creation timestamp
  - `updated_at`: Last modification timestamp
- **Purpose:** Represents platform users. Manages orders, carts, and account details.

### Category
- **Table Name:** `CATEGORY`
- **Primary Key:** `id`
- **Fields:**
  - `name`: Category label (e.g., "Electronics")
  - `description`: Brief classification details
  - `created_at`: Category creation timestamp
  - `updated_at`: Last modification timestamp
- **Purpose:** Organizes products into browseable/searchable groups.

### Product
- **Table Name:** `PRODUCT`
- **Primary Key:** `id`
- **Foreign Key:** `category_id` (references `CATEGORY.id`)
- **Fields:**
  - `name`: Product title
  - `description`: Item details
  - `price`: Cost value
  - `created_at`: Product creation timestamp
  - `updated_at`: Last modification timestamp
- **Purpose:** Represents purchasable items. Linked to categories and user interactions.

### Cart
- **Table Name:** `CART`
- **Primary Key:** `id`
- **Foreign Key:** `user_id` (references `USER.id`)
- **Fields:**
  - `created_at`: Cart creation timestamp
  - `updated_at`: Last modification timestamp
- **Purpose:** Stores pre-order product selections. Typically 1:1 with users.

### Cart Item
- **Table Name:** `CART_ITEM`
- **Primary Key:** `id`
- **Foreign Keys:**
  - `cart_id` (references `CART.id`)
  - `product_id` (references `PRODUCT.id`)
- **Fields:**
  - `quantity`: Selected product count
- **Purpose:** Individual product entries within carts.

### Order
- **Table Name:** `ORDER`
- **Primary Key:** `id`
- **Foreign Key:** `user_id` (references `USER.id`)
- **Fields:**
  - `order_date`: Purchase timestamp
  - `order_status`: Current state (e.g., "shipped")
  - `total_amount`: Order total cost
- **Purpose:** Captures finalized purchase details. Supports multiple items.

### Order Item
- **Table Name:** `ORDER_ITEM`
- **Primary Key:** `id`
- **Foreign Keys:**
  - `order_id` (references `ORDER.id`)
  - `product_id` (references `PRODUCT.id`)
- **Fields:**
  - `quantity`: Purchased product count
  - `unit_price`: Price at time of purchase
- **Purpose:** Breakdown of items within orders.

### Payment
- **Table Name:** `PAYMENT`
- **Primary Key:** `id`
- **Foreign Key:** `order_id` (references `ORDER.id`)
- **Fields:**
  - `amount`: Transaction value
  - `payment_date`: Payment timestamp
  - `payment_status`: Transaction state (e.g., "completed")
  - `payment_method`: Method used (e.g., "Credit Card")
- **Purpose:** Tracks financial transactions for orders.

---

## Relationships

- **User ↔ Cart**  
  `1-to-1`: Each user owns one cart. Carts require user association.

- **Cart ↔ Cart Item**  
  `1-to-Many`: One cart holds multiple items. Items link to one cart.

- **Product ↔ Cart Item**  
  `1-to-Many`: Products appear in multiple carts. Each item links to one product.

- **User ↔ Order**  
  `1-to-Many`: Users can place multiple orders. Orders link to one user.

- **Order ↔ Order Item**  
  `1-to-Many`: Orders contain multiple items. Items link to one order.

- **Product ↔ Order Item**  
  `1-to-Many`: Products appear in multiple orders. Items link to one product.

- **Order ↔ Payment**  
  `1-to-1`: Each order has one payment. (Extendable to `1-to-Many` for split payments)

- **Category ↔ Product**  
  `1-to-Many`: Categories contain multiple products. Products belong to one category.

---

## Future Considerations

- **Split Payments:** Convert Order-Payment relationship to `1-to-Many` if allowing partial payments.
- **Multi-Currency Support:** Add `currency` fields for international transactions.
- **Shipping Information:** Introduce `Shipping` entity/fields for addresses/tracking.
- **Inventory Management:** Add stock management via `Inventory` entity or product fields.