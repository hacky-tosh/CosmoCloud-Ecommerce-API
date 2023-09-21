# Ecommerce-API-App Using FAST Api

This is an Ecommerce Application built with Python and FastAPI.

## Overview

It provides various APIs for managing products, creating orders, and retrieving order information. The application utilizes a MongoDB database to store product and order data.

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


### Create a New Order
<br/>Endpoint: `api/orders`
<br/>Method: POST
<br/>Example Request:
```bash
POST http://localhost:8000/api/orders
Content-Type: application/json

{
  "timestamp": "2023-07-08T10:30:00",
  "items": [
    {
      "productId": "1",
      "boughtQuantity": 2
    },
    {
      "productId": "2",
      "boughtQuantity": 1
    }
  ],
  "totalAmount": 0.0,
  "userAddress": {
    "city": "Sample City",
    "country": "Sample Country",
    "zipCode": "12345"
  }
}

```

### Get All Orders
</br>Endpoint: `api/orders`
</br>Method: GET
</br>Example Request:
```bash
[
    {
        "timestamp": "2023-07-09T15:27:14.092011",
        "items": [
            {
                "productId": 1,
                "boughtQuantity": 2
            },
            {
                "productId": 2,
                "boughtQuantity": 1
            }
        ],
        "totalAmount": 1.0,
        "userAddress": {
            "city": "Sample City",
            "country": "Sample Country",
            "zipCode": "12345"
        }
    },
    {
        "timestamp": "2023-07-09T15:29:28.591415",
        "items": [
            {
                "productId": 1,
                "boughtQuantity": 2
            },
            {
                "productId": 2,
                "boughtQuantity": 1
            }
        ],
        "totalAmount": 3499.9700000000003,
        "userAddress": {
            "city": "Sample City",
            "country": "Sample Country",
            "zipCode": "12345"
        }
    }]
```

### Get Single Orders
</br>Endpoint: `api/orders/<id>`
</br>Method: GET

### Update Product
</br>Endpoint: `api/products/<product_id:int>`
</br>Method: GET
</br>Example Request:
```bash
PUT http://localhost:8000/api/products/1
Content-Type: application/json

{
    "id": 1,
    "name": "TV",
    "price": 999.99,
    "available_quantity": 20,
    "category": "Electronics"
}

```

