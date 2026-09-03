import datetime

VALID_CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Other"]

def validate_date(date_str):
    """Validates if the provided string matches the YYYY-MM-DD format."""
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_amount(amount_str):
    """Validates if the entry is a positive numerical value."""
    try:
        val = float(amount_str)
        return val > 0
    except ValueError:
        return False

def validate_category(category_str):
    """Checks if the category is valid and returns its standardized form."""
    normalized = category_str.strip().capitalize()
    if normalized in VALID_CATEGORIES:
        return normalized
    return None