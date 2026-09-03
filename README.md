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


<img width="1402" height="483" alt="Screenshot 2026-08-31 191823" src="https://github.com/user-attachments/assets/0de1d091-a47e-4242-8b61-cf3717f33edd" />
<img width="1421" height="587" alt="Screenshot 2026-08-31 191845" src="https://github.com/user-attachments/assets/ad8696e8-2987-4292-a14a-e6b5eb70eb3b" />
<img width="1281" height="548" alt="Screenshot 2026-08-31 192025" src="https://github.com/user-attachments/assets/0bb66e9f-7ba9-48b5-a0f9-fbc029a1cee1" />
<img width="802" height="548" alt="Screenshot 2026-08-31 192040" src="https://github.com/user-attachments/assets/f069d212-83e5-46d0-8d12-e6f2dc7f4a29" />
<img width="837" height="542" alt="Screenshot 2026-08-31 192148" src="https://github.com/user-attachments/assets/e38e2b2d-e8e3-4572-ba90-bd70cd06e315" />
<img width="786" height="491" alt="Screenshot 2026-08-31 192237" src="https://github.com/user-attachments/assets/42f61672-f78c-4179-bcde-51bf1eff322e" />
<img width="722" height="518" alt="Screenshot 2026-08-31 192250" src="https://github.com/user-attachments/assets/6bcfeca4-d720-4a06-a229-5228bc5e1628" />
