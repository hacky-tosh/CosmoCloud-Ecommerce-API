# CosmoCloud-Ecommerce-API

# Ecommerce Application

This is an Ecommerce Application built with Python and FastAPI.

## Overview

The Ecommerce Application is an online platform that allows users to browse and purchase products. It provides various APIs for managing products, creating orders, and retrieving order information. The application utilizes a MongoDB database to store product and order data.

## MongoDB Database

The application uses a MongoDB database to store product and order data. Make sure you have MongoDB installed and running on your system. Update the database connection details in the `.env` file.

## Installation

1. Clone the repository:
```bash
https://github.com/hacky-tosh/CosmoCloud-Ecommerce-API
```

3. Navigate to the project directory:
```bash
cd CosmoCloud-Ecommerce-API
```

4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

6. Ensure that MongoDB is installed and running on your system.
7. Create a MongoDB database for the application and update the database connection details in the `.env` file.

## Usage

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```
2. Access the API endpoints in your preferred API testing tool or web browser.

## APIs

The following APIs are available in the E-commerce Application:

### Get All Products

- Endpoint: `api/products`
- Method: GET
- Description: Retrieve all products from the db.
- Response:
 - Status: 200 OK
 - Body: List of products
Example
```bash
[
    {
        "id": 1,
        "name": "TV",
        "price": 500.0,
        "available_quantity": 10,
        "category": "Electronics"
    },
    {
        "id": 2,
        "name": "Laptop",
        "price": 1000.0,
        "available_quantity": 5,
        "category": "Electronics"
    }
]
```


