# Log Vault System (SQLite Learning Project)
This project demonstrates how to create, insert, and retrieve data from a SQLite database using Python.
It is intentionally simple and designed purely to help you understand how SQL works and how Python communicates with a database.

# Purpose
The system builds a LOGS table, inserts a message, and retrieves a specific log entry.
It teaches the fundamentals of SQL table creation, data insertion, and data selection.

## Features
- Connects to a local SQLite database (vault.db)
- Creates a LOGS table if it does not exist
- Inserts a single log message
- Retrieves a specific row (id = 1)
- Prints the result to the terminal
- Commits changes and closes the connection safely

## How it works
- A connection is opened to vault.db.
- A cursor is created to execute SQL commands.
- The LOGS table is created with:
  - id (auto‑increment primary key)
  - message (text field)
- A message is inserted into the table.
- The system selects the row where id = 1.
- The result is fetched and printed to the terminal.
- The database changes are committed.
- The connection is closed cleanly.


## Learning Purpose
This project helps practice:
- Creating tables with SQL
- Inserting data into a database
- Selecting specific rows
- Using cursors to execute SQL commands
- Understanding how SQLite stores and retrieves information
- Building confidence with SQL fundamentals
- It is a simple but effective training module for getting SQL “into your fingers.”
