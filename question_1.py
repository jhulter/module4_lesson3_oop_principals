class BudgetCategory:
    def __init__(self, category, budget):
        self._category = category
        self._budget = budget


    def get_category(self):
        return self._category

    def get_budget(self):
        return self._budget

    def set_category(self, new_category):
        self._category = new_category

    def set_budget(self, new_budget):
        self._budget = new_budget

    def add_expense(self):
        amount = int(input("Enter expense amount: "))
        self._budget -= amount

    def display_category_summary(self):
        print(f"You're viewing the category {self._category}...")
        print(f"Your budget is {self._budget}")




gas_category = BudgetCategory("Gas", 500)
gas_category.display_category_summary()
gas_category.add_expense()
gas_category.display_category_summary()
food_category = BudgetCategory("Food", 500)
food_category.display_category_summary()
food_category.add_expense()
food_category.display_category_summary()


