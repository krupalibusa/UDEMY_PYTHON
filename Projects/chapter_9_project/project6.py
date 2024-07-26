from income import IncomeManager
from expense import ExpenseTracker
from report import FinancialReport

def add_income(income_manager):
    print("\nAdd Income Source:")
    source_name = input("Enter income source name: ")
    amount = float(input("Enter amount: "))
    income_manager.add_income_source(source_name, amount)
    print(f"Added '{source_name}' with amount {amount}.")

def add_expense(expense_tracker):
    print("\nAdd Expense:")
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    expense_tracker.add_expense(category, amount)
    print(f"Added '{category}' expense with amount {amount}.")

def generate_reports(financial_report):
    print("\nFinancial Reports:")
    print("1. Generate Monthly Summary")
    print("2. Generate Expense Categories Report")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        summary = financial_report.generate_monthly_summary()
        print("\nMonthly Summary:")
        print("-----------------------------------------------------------------------------------")
        print(f"{'Total Income':<20}: ${summary['Total Income']}")
        print(f"{'Total Expenses':<20}: ${summary['Total Expenses']}")
        print(f"{'Savings':<20}: ${summary['Savings']}")
        print("-----------------------------------------------------------------------------------")
    elif choice == '2':
        expense_report = financial_report.generate_expense_categories_report()
        print("\nExpense Categories Report:")
        print("-----------------------------------------------------------------------------------")
        for category, amount in expense_report.items():
            print(f"{category:<20}: ${amount}")
        print("-----------------------------------------------------------------------------------")
    else:
        print("Invalid choice.")

def main():
    income_manager = IncomeManager()
    expense_tracker = ExpenseTracker()
    financial_report = FinancialReport(income_manager, expense_tracker)

    while True:
        print("\nPersonal Finance Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Generate Reports")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_income(income_manager)
        elif choice == '2':
            add_expense(expense_tracker)
        elif choice == '3':
            generate_reports(financial_report)
        elif choice == '4':
            print("Exiting Personal Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
