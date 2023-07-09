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
