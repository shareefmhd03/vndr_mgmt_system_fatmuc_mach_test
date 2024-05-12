# Vendor Management System

The Vendor Management System is a web application built using Django and Django REST Framework. It enables businesses to manage vendor profiles, track purchase orders, and evaluate vendor performance metrics.

## Features

### 1. Vendor Profile Management
- Create, update, retrieve, and delete vendor profiles.
- Each vendor profile includes information such as name, contact details, address, and a unique vendor code.

### 2. Purchase Order Tracking
- Create, update, retrieve, and delete purchase orders.
- Track purchase orders with fields like PO number, vendor reference, order date, items, quantity, and status.

### 3. Vendor Performance Evaluation
- Calculate and display performance metrics for each vendor.
  - On-Time Delivery Rate: Percentage of orders delivered by the promised date.
  - Quality Rating: Average of quality ratings given to a vendor’s purchase orders.
  - Response Time: Average time taken by a vendor to acknowledge or respond to purchase orders.
  - Fulfillment Rate: Percentage of purchase orders fulfilled without issues.

### 4. Authentication
- Token-based authentication for vendors.
- Vendors need to include their generated token in the HTTP headers to access the API endpoints.

## Installation

1. Clone the repository:

   ```bash
   https://github.com/shareefmhd03/vndr_mgmt_system_fatmug_mach_test.git

## Installation

```bash
    # 2. Install dependencies:
    pip install -r requirements.txt

    # 3. Apply migrations:
    python manage.py migrate

    # 4. Create a superuser (for accessing the Django admin):
    python manage.py createsuperuser

    # 5. Run the development server:
    python manage.py runserver

    ## Usage

    ```bash
        # View Swagger documentation for detailed API usage instructions.
        # Access Swagger UI at http://localhost:8000/docs/ when the server is running.
    ```
```

## API Endpoints

### Vendor Profile Management

- **POST /api/vendors/**: Create a new vendor profile.
- **GET /api/vendors/**: List all vendors.
- **GET /api/vendors/{vendor_id}/**: Retrieve details of a specific vendor.
- **PUT /api/vendors/{vendor_id}/**: Update a vendor's details.
- **DELETE /api/vendors/{vendor_id}/**: Delete a vendor profile.

### Purchase Order Tracking

- **POST /api/purchase_orders/**: Create a new purchase order.
- **GET /api/purchase_orders/**: List all purchase orders with an option to filter by vendor.
- **GET /api/purchase_orders/{po_id}/**: Retrieve details of a specific purchase order.
- **PUT /api/purchase_orders/{po_id}/**: Update a purchase order.
- **DELETE /api/purchase_orders/{po_id}/**: Delete a purchase order.

### Vendor Performance Evaluation

- **GET /api/vendors/{vendor_id}/performance/**: Retrieve performance metrics for a specific vendor.

### Authentication

Token-based authentication is used for vendors.
Vendors need to generate tokens using the Django management command (`drf_create_token`) and include them in the HTTP headers for authentication.
```bash
        python manage.py drf_create_token <vendor_username>\
```
    Authorization: Token <token_value>

