import csv
import os
import shutil
from datetime import datetime
from src.expense import Expense

DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "expenses.csv")

def ensure_data_dir():
    """Verifies that the target directory and the CSV file exist."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])

def load_expenses():
    """Loads records from the CSV file and converts them to Expense objects."""
    ensure_data_dir()
    expenses = []
    try:
        with open(FILE_PATH, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    expense = Expense(
                        amount=row['Amount'],
                        category=row['Category'],
                        date=row['Date'],
                        description=row['Description']
                    )
                    expenses.append(expense)
                except (ValueError, KeyError):
                    # Gracefully skip malformed rows without crashing
                    continue
    except FileNotFoundError:
        pass
    return expenses

def save_expenses(expenses):
    """Writes the full list of Expense objects back to the CSV."""
    ensure_data_dir()
    try:
        with open(FILE_PATH, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
            for exp in expenses:
                writer.writerow(exp.to_list())
    except IOError as e:
        print(f"Error saving data: {e}")

def backup_data():
    """Saves a dated copy of the CSV file inside data/backups/."""
    ensure_data_dir()
    if not os.path.exists(FILE_PATH):
        return False, "No data file exists yet to backup."
    
    backup_dir = os.path.join(DATA_DIR, "backups")
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"expenses_backup_{timestamp}.csv"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    try:
        shutil.copy(FILE_PATH, backup_path)
        return True, backup_path
    except IOError as e:
        return False, str(e)