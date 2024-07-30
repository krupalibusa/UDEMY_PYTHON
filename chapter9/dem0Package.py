from DemoPacakge import income , expesne

income.add_income(10000,"Salary")
income.add_income(20000,"Freelacing work")

expesne.add_expense(100,"Food")
expesne.add_expense(2000,"Rent")
expesne.add_expense(300,"Transpotation")

Total_expense = expesne.total_expense()

Total = income.total_income()
print("Total Income",Total)
print("Total Expense:", Total_expense)
print("Amount on Hand= ",Total - Total_expense)