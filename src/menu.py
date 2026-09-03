import sys
from datetime import date
from src.expense import Expense
from src.utils import validate_date, validate_amount, validate_category, VALID_CATEGORIES
from src import file_manager
from src import reports

def display_menu():
    print("\n" + "="*42)
    print("     PERSONAL FINANCE MANAGER")
    print("="*42)
    print("MAIN MENU:")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Category-wise Summary")
    print("4. Generate Monthly Report")
    print("5. Search Expenses")
    print("6. Backup Data")
    print("7. Exit")
    print("="*42)

def run_app():
    expenses = file_manager.load_expenses()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            add_expense_flow(expenses)
        elif choice == '2':
            view_expenses_flow(expenses)
        elif choice == '3':
            view_category_summary_flow(expenses)
        elif choice == '4':
            generate_monthly_report_flow(expenses)
        elif choice == '5':
            search_expenses_flow(expenses)
        elif choice == '6':
            backup_data_flow()
        elif choice == '7':
            print("\nExiting program. Goodbye!")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 7.")
        
        input("\nPress Enter to continue...")

def add_expense_flow(expenses):
    print("\nADD NEW EXPENSE:")
    
    # Amount Input
    while True:
        amount_str = input("Enter amount: ").strip()
        if validate_amount(amount_str):
            amount = float(amount_str)
            break
        print("❌ Invalid amount. Please enter a positive number.")
        
    # Category Input
    categories_str = "/".join(VALID_CATEGORIES)
    while True:
        category_input = input(f"Enter category ({categories_str}): ").strip()
        validated_cat = validate_category(category_input)
        if validated_cat:
            category = validated_cat
            break
        print(f"❌ Invalid category. Choose from: {categories_str}")
        
    # Date Input
    while True:
        date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if not date_str:
            date_str = date.today().strftime("%Y-%m-%d")
            break
        if validate_date(date_str):
            break
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        
    # Description Input
    description = input("Enter description: ").strip()
    if not description:
        description = "No description provided"
        
    new_expense = Expense(amount, category, date_str, description)
    expenses.append(new_expense)
    file_manager.save_expenses(expenses)
    print("\n✅ Expense added successfully!")

def view_expenses_flow(expenses):
    print("\nALL EXPENSES:")
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("-" * 65)
    print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 65)
    for exp in expenses:
        print(f"{exp.date:<12} | {exp.category:<15} | ₹{exp.amount:<9.2f} | {exp.description}")
    print("-" * 65)

def view_category_summary_flow(expenses):
    print("\nCATEGORY-WISE SUMMARY:")
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    summary = reports.generate_category_summary(expenses)
    total_all = sum(summary.values())
    
    print("-" * 40)
    print(f"{'Category':<18} | {'Total Spent':<15}")
    print("-" * 40)
    for cat, total in summary.items():
        print(f"{cat:<18} | ₹{total:<14.2f}")
    print("-" * 40)
    print(f"{'TOTAL':<18} | ₹{total_all:<14.2f}")

def generate_monthly_report_flow(expenses):
    print("\nGENERATE MONTHLY REPORT:")
    year_month = input("Enter Month (YYYY-MM): ").strip()
    
    # Basic structural check
    try:
        import datetime
        datetime.datetime.strptime(year_month, "%Y-%m")
    except ValueError:
        print("❌ Invalid format. Please enter as YYYY-MM.")
        return
        
    report = reports.generate_monthly_report(expenses, year_month)
    if not report:
        print(f"No records found for {year_month}.")
        return
        
    print("\n" + "="*40)
    print(f"      REPORT FOR {year_month}")
    print("="*40)
    print(f"Total Transactions: {report['count']}")
    print(f"Total Expenditure:  ₹{report['total']:.2f}")
    print(f"Average Expense:    ₹{report['average']:.2f}")
    print("-" * 40)
    print("Category Breakdown:")
    for cat, amount in report['breakdown'].items():
        pct = (amount / report['total']) * 100
        print(f"  - {cat:<12}: ₹{amount:<10.2f} ({pct:.1f}%)")
    print("="*40)

def search_expenses_flow(expenses):
    print("\nSEARCH EXPENSES:")
    query = input("Enter search keyword (category or description): ").strip()
    if not query:
        print("Empty search query.")
        return
        
    results = reports.search_expenses(expenses, query)
    if not results:
        print("No matching expenses found.")
        return
        
    print(f"\nFound {len(results)} matches:")
    print("-" * 65)
    for exp in results:
        print(exp)
    print("-" * 65)

def backup_data_flow():
    print("\nBACKING UP DATA...")
    success, result = file_manager.backup_data()
    if success:
        print(f"✅ Backup created successfully at:\n   {result}")
    else:
        print(f"❌ Backup failed: {result}")