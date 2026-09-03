class Expense:
    """Represents a single expense transaction."""
    
    def __init__(self, amount, category, date, description):
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        return f"{self.date} | {self.category}: ₹{self.amount:.2f} - {self.description}"

    def to_list(self):
        """Converts the object attributes to a list representation for CSV storage."""
        return [self.date, self.category, self.amount, self.description]