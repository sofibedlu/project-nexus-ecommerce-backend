## Feature Descriptions

Below is a high-level overview of each feature and its purpose:

| Feature                      | Description                                                                                                      |
|------------------------------|------------------------------------------------------------------------------------------------------------------|
| **User Authentication**      | Users can register/log in. JWT tokens are issued for secure backend interactions (cart/order management, etc.).  |
| **Category Management**      | Admins/privileged users perform CRUD operations on product categories (e.g., Electronics, Clothing).             |
| **Product Management**       | Manage products with attributes like name, description, price, and category linkage for organized browsing.      |
| **Filtering/Sorting/Pagination** | Users filter by category/attributes, sort by price, and view paginated results for efficient discovery.      |
| **Cart Management**           | Users maintain one active cart to add/update/remove items before converting to an order.                        |
| **Order Management**          | Converts carts to tracked orders with statuses (pending → shipped → delivered). Includes history/details.       |
| **Order Items**               | Tracks individual products in orders with quantities and unit prices for granular record-keeping.               |
| **Payment Handling**          | Records payment amount, method, date, and status (completed/failed). Linked to orders.                          |
| **API Documentation**         | Interactive Swagger/OpenAPI docs for all endpoints, streamlining frontend/third-party integration.              |

---

## Future Enhancements

- **Split Payments:** Enable 1:many Order-Payment relationships for partial/installment payments.  
- **Coupons & Discounts:** Add promo code support and dynamic discount logic at checkout.  
- **Inventory Management:** Track product stock levels and backorder capabilities.  
- **Shipping & Tracking:** Integrate logistics APIs for real-time shipping updates.  
- **Analytics & Reporting:** Generate business insights from order/payment/user activity data.  