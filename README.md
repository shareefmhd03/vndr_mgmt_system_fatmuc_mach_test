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
