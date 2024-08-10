# Test Results Report

## Overview
- **Project Name**: QA Challenge - Chicks Gold
- **Test Environment**: Testing
- **Due Date**: [07/30/2024]
- **Tester**: [Laura Moyano]

## Test Summary
| Metric | Count |
|--------|-------|
| Total Manual Tests | [67] |
| Passed | [10] |
| Failed | [57] |
| Pass Rate | [14.92%] |

## Failed Tests
| Test ID | Test Name | Error | Priority |
|---------|-----------|---------------|----------|
| [TC_005] | [Log out user] | [There is no "Logout" button] | [High] |
| ... | ... | ... | ... |
| [IDTC_006] | [Recover forgotten password] | [ No legend below the input with the option to recover password if forgotten] | [Medium] |
| ... | ... | ... | ... |
| [TC_007] | [Access to protected routes without authentication token is denied] | [Access without authentication tokens is allowed] | [High] |
| ... | ... | ... | ... |
| [TC_10] | [Create a new product with all required fields] | [There is not a "Create Product" button.The Product List is empty] | [High] |
| ... | ... | ... | ... |
| [TC_011] | [ Update information for an existing product] | [In the products page it only displays <h2>Product List</h2>. User cannot see an "Edit" button. User cannot see a "Save Changes" button. The Product List is empty and user can not add any product] | [High] |
| ... | ... | ... | ... |
| [TC_012] | [ Delete a product] | [In the products page it only displays <h2>Product List</h2>. There is no existing products in the Product List. User cannot see an "Delete" button] | [High] |
| ... | ... | ... | ... |
| [TC_013] | [Get list of all products] | [User cannot see product displayed] | [High] |
| ... | ... | ... | ... |
| [TC_0014] | [ Search products by category] | [User cannot see a category filter. User cannot see products displayed] | [High] |
| ... | ... | ... | ... |
| [TC_015] | [ Search products by name or description] | [User cannot see a search box. User cannot see products displayed] | [High] |
| ... | ... | ... | ... |
| [TC_016] | [Verify access to protected routes without authentication token] | [User is allowed to access "Products",  "Orders" and "Dashboard" routes without login. User is not redirected to the login page. No error message appears] | [High] |
| ... | ... | ... | ... |
| [TC_017] | [ Verify that only authorized users can modify products] | [There are no protected routes. User can acces before login and after. There is no denied access to unauthorized users ] | [High] |
| ... | ... | ... | ... |
| [TC_017] | [ Verify that only authorized users can modify products] | [There are no protected routes. User can acces before login and after. There is no denied access to unauthorized users ] | [High] |
| ... | ... | ... | ... |
| [TC_018] | [Create a new order with valid products] | [In the orders page it only displays <h2>Order List</h2>. User cannot see a shopping cart. User cannot see a checkout section. User cannot see a form to fill in order details. User cannot see a button to confirm the order] | [High] |
| ... | ... | ... | ... |
| [TC_019] | [Update the status of an order] | [There is no an order history. User cannot see an existing order. User cannot update an order. User cannot see a "Save changes" button] | [High] |
| ... | ... | ... | ... |
| [TC_020] | [Cancel an order] | [There is no an order history. User cannot see an existing order. User cannot create an order. User cannot see a "Cancel Order" button. User cannot see a button to confirm the cancellation] | [High] |
| ... | ... | ... | ... |
| [TC_021] | [Get list of orders from a user] | [There is no an order history. User cannot see a list of existing orders] | [High] |
| ... | ... | ... | ... |
| [TC_022] | [Get details of a specific order] | [There is no an order history. User cannot see an existing order. User cannot see order details] | [High] |
| ... | ... | ... | ... |
| [TC_023] | [Verify correct calculation of the order total] | [1. User cannot create an order. User cannot see a confirmation button. User cannot see products prices] | [High] |
| ... | ... | ... | ... |
| [TC_024] | [Process payment for an order (simulated)] | [ User cannot create a new order. User cannot see a payment section. User cannot see a form to fill payment details. User cannot see a button to confirm a payment] | [High] |
| ... | ... | ... | ... |
| [TC_025] | [Login with valid credentials] | [User is successful logged in but not redirected to the dashboard] | [High] |
| ... | ... | ... | ... |
| [TC_028] | [Log out from the dashboard] | [User cannot see a"Sign Out" nor a "Logout" button. User cannot log out  from the system] | [High] |
| ... | ... | ... | ... |
| [TC_030] | [Edit user profile information] | [User cannot see a profile section. User cannot see an "Edit Profile" or similar button. User cannot modify profile information. User cannot see a "Save the changes" button] | [High] |
| ... | ... | ... | ... |
| [TC_031] | [Verify that the dashboard displays relevant information ] | [Dashboard only displays the message "Welcome to the user dashboard!". Dashboard do not display any relevant information] | [High] |
| ... | ... | ... | ... |
| [TC_032] | [Verify user dashboard data display] | [Dashboard only displays the message "Welcome to the user dashboard!". Dashboard do not display any section nor information of the user activities] | [High] |
| ... | ... | ... | ... |
| [TC_033] | [Verify user dashboard data refresh] | [Dashboard only displays the message "Welcome to the user dashboard!". Dashboard do not display any relevant information. Dashboard do not have interactive components  (e.g., buttons)] | [High] |
| ... | ... | ... | ... |
| [TC_034] | [Load and display product list correctly] | [In the products page it only displays <h2>Product List</h2>. User cannot see products displayed. User cannot see pagination ] | [High] |
| ... | ... | ... | ... |
| [TC_035] | [Filter products by category] | [In the products page it only displays <h2>Product List</h2>. User cannot see products displayed. User cannot see categories] | [High] |
| ... | ... | ... | ... |
| [TC_036] | [Search products by name] | [User cannot see a product listing page. User cannot see a search field] | [High] |
| ... | ... | ... | ... |
| [TC_037] | [Add products to shopping cart] | [User cannot see a list of products. User cannot see an "Add to Cart" button. User cannot see a shopping cart. User cannot add products to the cart] | [High] |
| ... | ... | ... | ... |
| [TC_038] | [Modify quantity of products in the cart] | [User cannot see a list of products. User cannot see an "Add to Cart" button. User cannot see a shopping cart nor a cart page. User cannot add products to the cart. User cannot modify the quantity of products] | [High] |
| ... | ... | ... | ... |
| [TC_039] | [Remove products from cart] | [User cannot see a list of products. User cannot see a "Delete" or "Remove from Cart" button. User cannot delete a product from the cart] | [High] |
| ... | ... | ... | ... |
| [TC_040] | [Process an order from the cart] | [User cannot add products to cart. User cannot see a checkout page. User cannot see a form to fill in the necessary information (shipping address, payment method, etc.). User cannot confirm the order] | [High] |
| ... | ... | ... | ... |
| [TC_041] | [View order history] | [User cannot see an "Order History" section. User cannot see a list of previous orders] | [High] |
| ... | ... | ... | ... |
| [TC_042] | [View details of a specific order] | [User cannot see an order history page. User cannot select a specific order. User cannot view order details displayed] | [High] |
| ... | ... | ... | ... |
| [TC_043] | [ Verify that the products created in the backend appear in the Aurelia list] | [App is not connected to the backend. User do not have access to create products] | [High] |
| ... | ... | ... | ... |
| [TC_044] | [Check that orders placed in Aurelia are reflected in the ReactJS dashboard] | [User cannot shop products, they cannot see products nor buttons to interact with] | [High] |
| ... | ... | ... | ... |
| [TC_045] | [Ensure that order status changes on the backend will be updated in real time on the frontend] | [User cannot place orders, nor buy products] | [High] |
| ... | ... | ... | ... |
| [TC_046] | [Measure response time to load the product list with 100, 1000 and 10000 products] | [As a tester, I cannot load products on the page because there are no buttons nor interactivity in the Products and Orders pages] | [High] |
| ... | ... | ... | ... |
| [TC_047] | [Evaluate order processing time under load (50 simultaneous orders)] | [As a tester, I cannot load products on the page because there are no buttons nor interactivity in the Products and Orders pages] | [High] |
| ... | ... | ... | ... |
| [TC_048] | [Measure login time with 100 concurrent users] | [As a Tester I cannot execute this test because there is only one valid user] | [High] |
| ... | ... | ... | ... |
| [TC_049] | [Trying to access protected routes without authentication] | [TThere are no protected routes. When user logs in they are not redirected to any page] | [High] |
| ... | ... | ... | ... |
| [TC_050] | [Test SQL injection on lookup fields] | [The application is not connected to a database, so this threat does not affect it] | [High] |
| ... | ... | ... | ... |
| [TC_051] | [Verify the use of HTTPS in all communications] | [The application do not  use HTTPS, it is in localhost, but when it connects to the server it is on HTTP ] | [High] |
| ... | ... | ... | ... |
| [TC_052] | [Check secure password handling (hashing)] | [User password is hardcoded in the source code. It it not allowed to register a new user, nor change the password] | [High] |
| ... | ... | ... | ... |
| [TC_053] | [Try to manipulate product prices from the frontend] | [User cannot see products nor see or manipulate prices] | [High] |
| ... | ... | ... | ... |
| [TC_057] | [Verify that order totals are calculated correctly] | [Users cannot see product nor prices. Users cannot see a shopping cart] | [High] |
| ... | ... | ... | ... |
| [TC_058] | [Verify that inventory changes are appropriately reflected after orders] | [There is no inventory. User cannot place  an order for a product] | [High] |
| ... | ... | ... | ... |
| [TC_059] | [Ensure user information remains consistent between sessions] | [User cannot be their profile information. Session is stateless, so do not keep any information] | [High] |
| ... | ... | ... | ... |
| [TC_060] | [Evaluate the ease of navigation in the ReactJS dashboard] | [Users cannot complete basic tasks, as logging out, create products, place orders, see profile information, inventory nor past activity. Navigation structure is confusing] | [High] |
| ... | ... | ... | ... |
| [TC_061] | [Check the intuitiveness of the purchasing process in Aurelia] | [ 1. Users cannot complete a purchase] | [High] |
| ... | ... | ... | ... |
| [TC_062] | [Verify that error messages are clear and useful] | [There is only one error message, when login fail, and it i explains clearly the issue,  but do not explain how to solve it] | [Medium] |
| ... | ... | ... | ... |
| [TC_063] | [Verify product filtering algorithm] | [Both in the "ProductList.js" and in the "ProductController.cs" files, there is no algorithm that filters products by category] | [High] |
| ... | ... | ... | ... |
| [TC_064] | [Validate shopping cart total calculation] | [Both in the "OrderList.js" and in the "OrderController.cs" files, there is no algorithm that adds products to cart] | [High] |
| ... | ... | ... | ... |
| [TC_065] | [ Check order processing workflow] | [The system does not have implemented all the methods needed in a complete CRUD an user cannot do any of the operations, the only functionality implemented in the frontend is user log in] | [High] |
| .name.. | ... | ... | ... |
| [TC_066] | [Evaluate authentication middleware] | [The system lacks of authentication middleware. Valid username and password are hardcoded] | [High] |
| ... | ... | ... | ... |
| [TC_067] | [Test database connection pool management] | [The system does not have implemented a database connection and it is stateless, does not keep any information and when the application restarts all the information disappears] | [High] |
| ... | ... | ... | ... |

## Issues and Risks

-  I started up the application in Visual Studio because is the IDE by default of C# and .NET, and a critical fail, ocurred, that I reported in the "Issues" folder.
- When I started up the application in Visual Studio Code it did not fail, but I coud not connect qa-app with qa-api.
- A risk security alert popped up in Google Chrome. I leave all the screenshots in Images folder but I am not sure If I will be able to finnish the report at the required time. But I will finnish it anyway.
- There are security breaches that I recorded in the Test Cases, (e.g. it lacks of an HTTPS protocol) but as this application is not working in a production environment, is not connected to a database and has hardcoded user credentials, I understand that many of the threats will not affect it.

# Recommendations for Application Improvement

## 1. Functionalities:

- Implement a function that after successful login, user is redirected to the dashboard
- Implement functionalities in the dashboard:
 + User profile (with CRUD operatios to modify, delete account and see information)
 + User activity history
 + List of saved and purchased products 

- Implement functionalities in the products page:
 + List products by category
 + See products availables list with their respectives, descriptions and prices
 + Shopping cart to add products with proper CRUD operations
 + Filters to search for products and to order products with different criteria 
  + See images of products displayed

- Implement functionalities in the orders page:
 + See orders with deatailed data (product, price, image seller, shipping data)
 + Implement CRUD operations to process orders
 + Implement a checkout page with payment gateway

- Complete the CRUD methods implemented
- Properly connect the API to the app
- Make sure all buttons needed are implemented.

## 1. Performance Optimization
- Implement caching mechanisms for frequently accessed data
- Use asynchronous programming where appropriate to improve responsiveness

## 2. Security Enhancements
- Implement proper authentication and authorization mechanisms
- Use HTTPS for all communications
- Regularly update dependencies to patch known vulnerabilities
- Implement input validation and sanitization to prevent injection attacks

## 3. Code Quality
- Implement a consistent coding style guide
- Increase unit test coverage
- Use static code analysis tools to identify potential issues

## 4. User Experience
- Improve UI/UX design based on user feedback
- Add clear error messages and user-friendly notifications
- Add buttons needed

## 5. Scalability
- Design the architecture to be horizontally scalable

## 6. Monitoring and Logging
- Implement comprehensive logging throughout the application
- Set up real-time monitoring and alerting systems
- Use analytics to track user behavior and application performance

## 7. Documentation
- Improve inline code documentation
- Create and maintain up-to-date API documentation
- Develop a comprehensive user guide and FAQ section

## 8. Continuous Integration/Continuous Deployment (CI/CD)
- Implement automated testing in the CI pipeline
- Set up automated deployment processes

## 9. Accessibility
- Ensure the application meets WCAG guidelines
- Implement keyboard navigation support

## 10. Internationalization and Localization
- Implement multi-language support
- Adapt the application for different cultural contexts

## 11. Data Management
- Implement a robust backup and recovery system
- Implement database connection

## 13. Error Handling
- Implement a centralized error handling mechanism
- Create a system for categorizing and prioritizing errors
- Set up error reporting and analysis tools

## 14. Performance Testing
- Conduct regular load testing to identify bottlenecks
- Implement stress testing to understand system limits
- Use profiling tools to identify performance issues in the code

## Conclusion
[This has been such a great expierience. Beyond what happens I want to express my gratitude with all the team. I felt very comfortable and excited these days. 

I had not ever used Visual Studio, nor worked with C# or .NET but I really liked to. I remember that Mercy told us that you use Azure and, as I studied Azure last year, I attempted to use Azure DevOps to make the test plan, test cases and report, but as I have a student account, I do not have permissions to use it so I could not. I decided to work in Excel. Markdown is a language that I had not used but I guess it is more accurated for GitHub so I investigated how to use it.

I uploaded all the screenshots of the testing to the "Images" folder. I used Chrome DevTools to test accesibility, performance, responsiveness and SEO, Lighthouse for the audits and metrics and Swagger UI to see the endpoints implemented. 




]

## Approvals
- **Tested By**: [Laura Moyano] - [07/30/2024]

---

## Appendix
### Test Environment Details
- **Operating System**: [Windows 10 Pro 64-bits]
- **Browser(s)**: [Google Chrome Version 127.0.6533.73 (Official Build) (64-bit), Microsoft Edge Versión 127.0.2651.74 (Official Build) (64 bits)]
- **Device(s)**: [Laptop Dell Latitude E6530]
