# Test Cases

## Backend (C# API):

1. **User authentication:**

+ Sign in with valid credentials
+ Try to log in with invalid credentials
+ Log out user
+ Recover forgotten password
+ Verify authentication token for access to protected routes

2. **Product management:**

+ Create a new product with all required fields
+ Update information for an existing product
+ Delete a product
+ Get list of all products
+ Search products by category
+ Search products by name or description
+ Verify that only authorized users can modify products

3. **Order processing:**

+ Create a new order with valid products
+ Update the status of an order
+ Cancel an order
+ Get list of orders from a user
+ Get details of a specific order
+ Verify correct calculation of the order total
+ Process payment for an order (simulated)

## Interface:

1. **ReactJS - User Authentication and Dashboard:**

+ Login with valid credentials
+ Show success message for successful login
+ Show error message for invalid credentials
+ Sign out from the dashboard
+ View user profile information
+ Edit user profile information
+ Verify that the dashboard displays relevant information (order summary, etc.)
+ Verify user dashboard data display
+ Verify user dashboard data refresh

2. **Aurelia - Product listing and order processing:**

+ Load and display product list correctly.
+ Filter products by category
+ Search products by name
+ Add products to shopping cart
+ Modify quantity of products in the cart
+ Remove products from cart
+ Process an order from the cart
+ View order history
+ View details of a specific order

## Integration testing:

+ Verify that the products created in the backend appear in the Aurelia list
+ Check that orders placed in Aurelia are reflected in the ReactJS dashboard
+ Ensure that order status changes on the backend will be updated in real time on the frontend

## Test of performance:

+ Measure response time to load the product list with 100, 1000 and 10000 products
+ Evaluate order processing time under load (50 simultaneous orders)
+ Measure login time with 100 concurrent users

## Security tests:

+ Trying to access protected routes without authentication
+ Test SQL injection on lookup fields
+ Verify the use of HTTPS in all communications
+ Check secure password handling (hashing)
+ Try to manipulate product prices from the frontend.

## Compatibility tests:

+ Check functionality in Chrome, Firefox, Safari and Edge
+ Test responsiveness on mobile devices (iOS and Android)
+ Check display on different screen sizes

## Data integrity testing:

+ Verify that order totals are calculated correctly
+ Verify that inventory changes are appropriately reflected after orders
+ Ensure user information remains consistent between sessions

## Usability tests:

+ Evaluate the ease of navigation in the ReactJS dashboard
+ Check the intuitiveness of the purchasing process in Aurelia
+ Verify that error messages are clear and useful

## White Box Testing:

+ Verify product filtering algorithm
+ Validate shopping cart total calculation
+  Check order processing workflow
+ Evaluate authentication middleware
+ Test database connection pool management