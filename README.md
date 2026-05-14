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
📂 FOLDER: Module mixed project
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
📂 FOLDER: Module mixed project
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
🛠 TECHNOLOGIES USED
==================================================

• Python
• SQLite3
• Pydantic
• Requests
• BeautifulSoup4
• JSON
• Tracemalloc

