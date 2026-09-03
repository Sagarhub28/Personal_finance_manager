# Personal Finance Manager

A modular, terminal-based personal finance management application written in Python. This utility helps users track daily expenses, categorize transactions, generate monthly summary reports, perform text-based searches, and maintain localized backups of their records.

---

## 📌 Project Overview
The Personal Finance Manager is designed to run efficiently inside a terminal environment. Built on Object-Oriented Programming (OOP) principles, it enforces robust input validation, processes data collections dynamically, and persists information locally using CSV files.

### Key Features
* **Interactive Command Line Interface**: A structured menu system allowing quick navigation.
* **Robust Input Validation**: Strict validation for amounts, standard dates (YYYY-MM-DD), and predefined categories.
* **File Operations & Persistence**: Automatically handles directories and persists records in a comma-separated values (CSV) database.
* **Detailed Reporting & Search**: Calculates total and average expenditures, produces category percentage breakdowns, and performs text queries across descriptions.
* **Automated Data Backups**: Exports dated backup files to a dedicated path for redundancy.
* **Unit Tested Logic**: Includes automated test assertions for core validations and analytics helpers.

---

## 📁 Code Structure
The project files are arranged according to the following directory layout:

```text
personal_finance_manager/
│
├── main.py                # Main entry point for the application
├── README.md              # Project documentation and setup guide
├── requirements.txt       # Dependencies (optional)
├── .gitignore             # Tells Git which files to exclude from tracking
│
├── data/                  # Local database folder (auto-created)
│   ├── expenses.csv       # Active database file
│   └── backups/           # Auto-generated backup copies
│
├── tests/                 # Automated testing scripts
│   └── test_finance.py    # Unit tests for validation & reporting
│
└── src/                   # Core application source code
    ├── __init__.py        # Designates 'src' as a Python package
    ├── expense.py         # Defines the OOP Expense class
    ├── file_manager.py    # Implements file read/write and backup logic
    ├── menu.py            # Implements UI screens and application flows
    ├── reports.py         # Handles grouping, summaries, and search math
    └── utils.py           # Includes input verification & normalization

---

## 2. Setup & Installation Guide

Follow these steps to configure your environment and run the system.

### Prerequisites
* **Python 3.8+**: Ensure Python is installed. Check by running `python --version` in your terminal.
* **Operating System**: Compatible with Windows, macOS, and Linux.

### Step-by-step Setup
1. **Create the Project Folder**:
   Create a directory on your machine:
   ```bash
   mkdir personal_finance_manager
   cd personal_finance_manager



