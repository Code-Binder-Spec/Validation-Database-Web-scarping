==================================================
 VALIDATION • DATABASE • WEB SCRAPING PROJECTS
==================================================

A collection of Python learning projects focused on:

• Data Validation
• SQLite Database Systems
• Backend Logic
• Web Scraping
• Error Handling
• Structured Data Processing

Each project in this repository was built to practice real programming concepts through hands-on development instead of only theoretical learning.

==================================================
📂 FOLDER: Database
📦 PROJECT 01 — Batch_order_system.py
==================================================

TYPE:
Backend Style Order Processing System

DESCRIPTION:
A beginner-level Python project that simulates an order management workflow.

The system validates customer data, processes orders, checks balances, generates unique order IDs, and stores confirmed orders inside an SQLite database.

MAIN FEATURES:
✔ User validation using Pydantic
✔ Product ordering workflow
✔ Balance checking system
✔ Automatic order ID generation
✔ SQLite database storage
✔ Structured backend-style logic

DATABASE:
orders.db

LEARNING FOCUS:
- Validation systems
- Backend logic flow
- Database persistence
- Class-based structure
- Order processing systems

==================================================
📂 FOLDER: Scraping
🌐 PROJECT 02 — Quotes_scrape.py
==================================================

TYPE:
Web Scraping & Data Collection System

DESCRIPTION:
A Python scraping project that collects quotes and author names from Quotes to Scrape using Requests and BeautifulSoup.

The scraper processes multiple pages, extracts HTML data, stores results inside a JSON file, and tracks memory usage during execution.

MAIN FEATURES:
✔ Multi-page scraping
✔ HTML parsing with BeautifulSoup
✔ JSON file storage
✔ Generator-based data handling
✔ Error protection for failed requests
✔ Memory tracking using tracemalloc
✔ Execution statistics display

OUTPUT:
quotes.json

LEARNING FOCUS:
- Web scraping
- HTML parsing
- Generators
- Error handling
- Memory optimization
- JSON processing

==================================================
📂 FOLDER: Database
🎬 PROJECT 03 — Movie_database.py
==================================================

TYPE:
Command-Line Movie Management System

DESCRIPTION:
A terminal-based movie database system built using Python, SQLite, and Pydantic.

The system allows users to add, update, view, and delete movies while enforcing strong validation rules.

MAIN FEATURES:
✔ Add movies
✔ Show all movies
✔ Show top-rated movies
✔ Update movie ratings
✔ Delete movies
✔ SQLite database integration
✔ Validation using Pydantic

DATABASE:
Movies.db

VALIDATION RULES:
• Movie name cannot be empty
• Ratings must be between 0 and 10
• Invalid movie years are rejected

LEARNING FOCUS:
- CRUD operations
- Database handling
- Data validation
- Terminal applications
- Persistent storage systems

==================================================
📂 FOLDER: Scraping
📦 PROJECT 02 — Book_scrape.py
==================================================

TYPE:
Memory Optimized Web Scraping & Validation System

DESCRIPTION:

A Python-based web scraping project that extracts book data from multiple pages, validates the extracted information using Pydantic, and stores the cleaned results inside a JSON file.

The project uses a generator-based pipeline architecture to reduce memory usage while processing large amounts of scraped data. It also tracks RAM usage using tracemalloc.

MAIN FEATURES:

✔ Multi-page web scraping using Requests
✔ HTML parsing using BeautifulSoup
✔ Data validation using Pydantic
✔ Generator-based streaming pipeline
✔ Memory optimized JSON writing
✔ Automatic book categorization
✔ Exception handling for failed requests
✔ RAM usage tracking using tracemalloc
✔ Structured modular function design

OUTPUT FILE:

books.json

LEARNING FOCUS:

Web scraping workflows
Generator pipelines
Memory optimization
Streaming JSON writing
Data validation systems
Exception handling
HTML parsing
Backend-style data processing
Modular architecture

==================================================
📂 FOLDER: Combined
📦 PROJECT 01 — Job_info.py
==================================================
TYPE: 
Real-World Job Board Web Scraping & SQLite Storage System

DESCRIPTION:
A Python-based web scraping project that extracts job listing data from the Python.org job board,
validates the extracted information using Pydantic, and stores the cleaned results inside a SQLite database.
The project targets a real-world, inconsistently structured job board — making it significantly
more complex than tutorial-grade scraping projects. It uses a generator-based pipeline architecture
to process data efficiently, with multi-level defensive extraction to handle missing or malformed HTML fields.

MAIN FEATURES:
✔ Real-world job board scraping using Requests
✔ HTML parsing using BeautifulSoup
✔ Scoped CSS selector extraction (container-based)
✔ Multi-level defensive chaining for missing tags
✔ Data validation using Pydantic
✔ Generator-based streaming pipeline
✔ Job description extraction from nested HTML structure
✔ SQLite database storage using sqlite3
✔ Exception handling for failed requests and bad listings
✔ Safe database connection management using try/except/finally
✔ Structured modular function design

OUTPUT FILE:
Job.db

LEARNING FOCUS:
Real-world web scraping on inconsistent HTML
CSS selector scoping and descendant selectors
Defensive chaining for missing/null tags
Generator pipelines and memory efficiency
Data validation with Pydantic model validators
SQLite database creation and insertion
Safe resource management with try/except/finally
Modular pipeline architecture
Handling optional and unreliable data fields

==================================================
🛠 TECHNOLOGIES USED
==================================================

• Python
• SQLite3
• Pydantic
• Requests
• BeautifulSoup4
• JSON
• Tracemalloc

