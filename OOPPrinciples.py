class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self._category_name = category_name
        self._allocated_budget = allocated_budget
        self._expenses = 0
    
    def get_category_name(self):
        return self._category_name

    def set_category_name(self, new_category_name):
        self._category_name = new_category_name

    def get_allocated_budget(self):
        return self._allocated_budget

    def set_allocated_budget(self, new_allocated_budget):
        if new_allocated_budget > 0:
            self._allocated_budget = new_allocated_budget
        else:
            print("Budget should be a positive number.")

    def add_expense(self, amount):
        if amount > 0:
            if self._allocated_budget >= amount:
                self._expenses += amount
                self._allocated_budget -= amount
                print("Expense added successfully.")
            else:
                print("Expense amount exceeds the allocated budget.")
        else:
            print("Expense amount should be a positive number.")

    def get_expenses(self):
        return self._expenses

category1 = BudgetCategory("Takeout", 500)
category2 = BudgetCategory("Streaming Services", 100)

print(category1._category_name)  
print(category1._allocated_budget)  

print(category2._category_name)  
print(category2._allocated_budget)  