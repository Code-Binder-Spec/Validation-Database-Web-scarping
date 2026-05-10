# Validation-Database-Web-Scraping

This repository is a collection of my practice and project-based code covering validation systems, database handling, and web scraping techniques. It serves as a central workspace where I experiment with different concepts, build small utilities, and improve my programming skills over time. The repository may contain multiple independent scripts and modules, each focusing on a specific task or learning objective within these domains.

Batch_order_system.py
---------------------
This project is a beginner-level Python system that simulates an order processing workflow. It handles user validation, order creation, and stores order data in a local SQLite database.

The system uses structured data models with Pydantic for input validation and ensures that only valid user details and orders are processed. Each order includes user information, address details, product selection, balance checking, and automatic order ID generation.

At the moment, this project does not use APIs or external services. All data is generated locally within the script and processed in a controlled environment. The main focus of this project is to understand how backend-style systems work, including validation, data flow, and database storage.

The project stores all confirmed orders in an SQLite database (orders.db) for persistence and later retrieval.

This is a learning-stage project focused on:

Data validation concepts
Basic backend structure
SQLite database usage
Order processing logic
Python class-based modeling
