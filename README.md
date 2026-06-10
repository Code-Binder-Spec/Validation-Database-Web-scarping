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
📂 FOLDER: Database/normal_sqlite
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
📂 FOLDER: Scraping/normal_scraping
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
📂 FOLDER: Database/normal_sqlite
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
📂 FOLDER: Scraping/normal_scraping
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
📂 FOLDER: Scraping/aiohttp_scraping
📦 PROJECT — Hackernews_scraping.py
==================================================
TYPE:
Async Multi-Page Hacker News Scraper with JSON Storage

DESCRIPTION:
A Python-based asynchronous web scraping project that extracts story data
from 30 pages of Hacker News simultaneously using aiohttp and asyncio.
The project uses a Semaphore-controlled concurrency model to avoid
overwhelming the server, with defensive extraction handling missing or
inconsistent HTML fields. Scraped data is validated at the extraction
level and stored in a structured JSON output file with full logging support.

MAIN FEATURES:
✔ Asynchronous HTTP requests using aiohttp
✔ Concurrent scraping of 30 pages using asyncio.gather
✔ Semaphore-based rate limiting (max 3 concurrent requests)
✔ HTML parsing using BeautifulSoup
✔ Modular defensive extraction for title, score, and comment fields
✔ Sibling-row parsing for Hacker News two-row story structure
✔ Exception handling for failed requests and bad status codes
✔ Structured JSON output storage
✔ File-based logging with DEBUG level tracking
✔ Clean session management using aiohttp.ClientSession

OUTPUT FILE:
Hackernews.json
Hackernews.log

LEARNING FOCUS:
Asynchronous programming with asyncio and aiohttp
Semaphore-based concurrency control
Multi-page parallel scraping architecture
Defensive extraction for inconsistent HTML structures
Sibling-row parsing for paired HTML elements
Modular scraping function design
JSON data storage and formatting
File-based logging for async applications
Exception handling in async context

==================================================
📂 FOLDER: Database/aiosqlite
📦 PROJECT — Banking_system.py
==================================================
TYPE:
Async Banking System with SQLite Storage and Transaction Management

DESCRIPTION:
A Python-based asynchronous banking system that simulates real-world financial
operations including deposits, withdrawals, and transfers using aiosqlite and asyncio.
The project uses a multi-table SQLite database to persist account and transaction
data, with a whitelist-based SQL injection defense layer for dynamic queries.
All operations are processed concurrently using asyncio.gather, with full rollback
support on failure and structured transaction logging for every operation attempted.

MAIN FEATURES:
✔ Asynchronous SQLite operations using aiosqlite
✔ Concurrent transaction processing using asyncio.gather
✔ Multi-table database design (accounts + transactions)
✔ Deposit, Withdraw, and Transfer operations
✔ Whitelist-based SQL injection defense for dynamic queries
✔ Atomic transactions with rollback on failure
✔ Transaction status logging (Success/Failed) in database
✔ Defensive balance validation before operations
✔ Structured process router for transaction dispatch
✔ Safe database connection management using async context manager

OUTPUT FILE:
Bank.db

LEARNING FOCUS:
Asynchronous database operations with aiosqlite
Concurrent transaction handling with asyncio.gather
Multi-table relational database design
Atomic transactions and rollback strategies
Whitelist-based defense against SQL injection
Balance validation and financial logic
Transaction logging and status tracking
Async context manager for database connections
Dynamic query construction with safety constraints
Modular async function architecture

Readme · TXT
==================================================
📂 FOLDER: Combined
📦 PROJECT — github_scraping.py
==================================================
TYPE:
Async GitHub Trending Scraper with Pydantic Validation and SQLite Storage
 
DESCRIPTION:
A Python-based asynchronous web scraper that collects trending repository data
from GitHub across daily, weekly, and monthly time periods using aiohttp and
BeautifulSoup. Scraped data is validated and type-coerced through a Pydantic
model before being persisted to a SQLite database via aiosqlite. All three
time period pages are fetched concurrently using asyncio.gather with a semaphore
to control request rate. The pipeline includes per-repo error handling, structured
logging to a log file, and deduplication via a UNIQUE constraint to ensure safe
repeated runs without duplicate rows.
 
MAIN FEATURES:
✔ Asynchronous HTTP fetching using aiohttp
✔ Concurrent scraping of daily, weekly, and monthly trending pages via asyncio.gather
✔ Rate-limiting with asyncio.Semaphore to avoid overwhelming GitHub
✔ HTML parsing with BeautifulSoup across modular scraper functions
✔ Pydantic model with field validators for type coercion and cleaning
✔ Handles optional fields (language, description) with None fallback
✔ Cleans star/fork counts from formatted strings to integers
✔ Async SQLite storage using aiosqlite
✔ Deduplication via UNIQUE(username, reponame, time_period) constraint
✔ INSERT OR IGNORE to safely skip duplicate rows on repeated runs
✔ Per-repo exception handling with continue logic to avoid pipeline crash
✔ Structured logging to file for success and failure tracking
 
OUTPUT FILE:
githubdata.db
 
LEARNING FOCUS:
Asynchronous HTTP requests with aiohttp
Concurrent coroutine execution with asyncio.gather
Semaphore-based concurrency control
Real-world HTML parsing with BeautifulSoup
Pydantic v2 field validators with mode="before"
Type coercion and optional field handling in Pydantic
Async SQLite operations with aiosqlite
Deduplication strategy with UNIQUE constraints
Error isolation per repo with try/except and continue
Logging to file with Python's logging module
End-to-end async data pipeline architecture

==================================================
📂 FOLDER: Combined
📦 PROJECT — flipkart_scraper.py
==================================================
TYPE:
Async Flipkart Product Scraper with Pydantic Validation and SQLite Storage

DESCRIPTION:
A Python-based asynchronous web scraper that collects product data from Flipkart
search result pages using aiohttp and BeautifulSoup. The scraper fetches up to 30
pages concurrently with a Semaphore-controlled request rate to avoid bot detection.
Each product's raw data is validated and type-coerced through a Pydantic model
before being persisted to a SQLite database via aiosqlite. The pipeline includes
per-field error handling with flag-based fallbacks, structured logging to a file,
and deduplication via a UNIQUE constraint to ensure safe repeated runs.

MAIN FEATURES:
✔ Asynchronous HTTP fetching using aiohttp with custom browser headers
✔ Concurrent multi-page scraping (up to 30 pages) via asyncio.gather
✔ Rate-limiting with asyncio.Semaphore to avoid triggering bot detection
✔ Modular scraper functions per field (name, price, features, rating, reviews)
✔ Flag-based error isolation — failed fields return fallback values, not crashes
✔ Pydantic v2 model with field validators for type coercion and None handling
✔ Handles optional fields (price, features, rating) with None fallback
✔ Cleans rating and review counts from formatted strings to float/int
✔ Async SQLite storage using aiosqlite
✔ Deduplication via UNIQUE(name, price) constraint
✔ INSERT OR IGNORE to safely skip duplicate rows on repeated runs
✔ Structured logging to file for per-field scraping failures

OUTPUT FILE:
flipkart.db

LEARNING FOCUS:
Asynchronous HTTP requests with aiohttp
Custom request headers for bot detection bypass
Concurrent page scraping with asyncio.gather
Semaphore-based concurrency control
Modular scraper architecture with per-field functions
Flag-based error handling without pipeline crashes
Pydantic v2 field validators with mode="before"
Optional field handling with None fallback values
Type coercion from strings to float and int
Async SQLite operations with aiosqlite
Deduplication strategy with UNIQUE constraints
Structured logging to file with Python logging module

==================================================
🛠 TECHNOLOGIES USED
==================================================

- Python
- SQLite3
- Pydantic
- Requests
- BeautifulSoup4
- aiohttp
- aiosqlite
- asyncio
- JSON
- Tracemalloc
- Logging
