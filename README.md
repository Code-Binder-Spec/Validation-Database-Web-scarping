# Validation-Database-Web-Scraping

This repository is a collection of my practice projects and learning experiments focused on validation systems, database handling, and web scraping using Python.

The repository contains multiple independent scripts and mini-projects built to improve my understanding of backend logic, structured validation, database persistence, data processing, and scraping workflows.

The main purpose of this repository is to strengthen problem-solving skills and gain practical experience by building real working systems instead of only studying theory.

==================================================
TECHNOLOGIES USED
==================================================

- Python
- SQLite3
- Pydantic
- Requests
- BeautifulSoup4
- JSON
- Tracemalloc

==================================================
PROJECTS INCLUDED
==================================================

##################################################
MODULE MIXED PROJECT / Batch_order_system.py
##################################################

OVERVIEW
--------------------------------------------------

This project is a beginner-level Python order processing system that simulates a backend-style workflow for handling customer orders.

The system validates user information, creates orders, processes product selections, checks balances, and stores confirmed orders inside a local SQLite database.

The project focuses on understanding how backend systems manage data flow, validation, and persistent storage.

FEATURES
--------------------------------------------------

[✓] User Validation
Validates customer information before processing orders.

[✓] Product Ordering
Allows users to select products and create orders.

[✓] Balance Checking
Checks whether the customer has enough balance before confirming the order.

[✓] Automatic Order ID Generation
Generates unique order IDs automatically.

[✓] SQLite Database Storage
Stores confirmed orders inside:

orders.db

[✓] Structured Validation
Uses Pydantic models to ensure valid and safe data handling.

LEARNING FOCUS
--------------------------------------------------

- Data validation concepts
- Backend-style logic flow
- SQLite database handling
- Order processing systems
- Class-based Python structure
- Persistent data storage

##################################################
SCRAPING / Quotes_scrape.py
##################################################

OVERVIEW
--------------------------------------------------

This project is a Python web scraping system that collects quotes and author names from Quotes to Scrape using Requests and BeautifulSoup.

The scraper processes multiple pages, extracts quote data from HTML, and stores the collected information inside a local JSON file.

The project also tracks memory usage and request statistics during execution.

FEATURES
--------------------------------------------------

[✓] Multi-page Scraping
Scrapes quotes from multiple pages automatically.

[✓] HTML Parsing
Uses BeautifulSoup to extract quotes and author names from HTML content.

[✓] JSON Storage
Stores scraped data inside a JSON file for later use.

[✓] Generator Functions
Uses generators for efficient memory handling.

[✓] Error Handling
Skips failed requests without stopping the entire scraping process.

[✓] Memory Tracking
Tracks RAM usage using tracemalloc.

[✓] Execution Statistics
Displays:
- Total URLs fetched
- Successful requests
- Total quotes collected
- Peak memory usage

LEARNING FOCUS
--------------------------------------------------

- Web scraping
- HTML parsing
- Generators
- Nested looping
- Error handling
- JSON handling
- Memory optimization
- Python data flow understanding

##################################################
MODULE MIXED PROJECT / Movie_database.py
##################################################

OVERVIEW
--------------------------------------------------

A command-line Movie Management System built using Python, SQLite, and Pydantic.

The project allows users to manage a movie database directly from the terminal while maintaining strong validation and persistent storage.

FEATURES
--------------------------------------------------

[✓] Add Movies
Store movie name, release year, and rating inside a SQLite database.

[✓] Show All Movies
Displays all stored movies.

[✓] Show Top Movies
Displays the top 3 highest-rated movies.

[✓] Update Ratings
Update ratings for existing movies.

[✓] Delete Movies
Remove movies from the database.

[✓] Data Validation
Validation handled using Pydantic:
- Empty movie names are rejected
- Ratings must be between 0 and 10
- Invalid movie years are rejected

[✓] SQLite Database Storage
Automatically creates and manages:

Movies.db

LEARNING FOCUS
--------------------------------------------------

- SQLite database handling
- Data validation
- CRUD operations
- Database persistence
- Python terminal applications
- Structured backend logic

==================================================
