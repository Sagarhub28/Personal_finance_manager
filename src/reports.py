def generate_category_summary(expenses):
    """Groups expenses by category and returns totals."""
    summary = {}
    for exp in expenses:
        summary[exp.category] = summary.get(exp.category, 0.0) + exp.amount
    return summary

def generate_monthly_report(expenses, year_month):
    """Filters expenses matching YYYY-MM and calculates key metrics."""
    monthly_expenses = [exp for exp in expenses if exp.date.startswith(year_month)]
    
    if not monthly_expenses:
        return None
    
    total = sum(exp.amount for exp in monthly_expenses)
    average = total / len(monthly_expenses)
    
    category_breakdown = {}
    for exp in monthly_expenses:
        category_breakdown[exp.category] = category_breakdown.get(exp.category, 0.0) + exp.amount
        
    return {
        "total": total,
        "average": average,
        "count": len(monthly_expenses),
        "breakdown": category_breakdown
    }

def search_expenses(expenses, query):
    """Finds items containing the search query in category or description."""
    query = query.lower()
    return [
        exp for exp in expenses 
        if query in exp.category.lower() or query in exp.description.lower()
    ]