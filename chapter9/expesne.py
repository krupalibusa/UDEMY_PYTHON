expense = []

def add_expense(amount,source):
    expense.append({"Source":source,"Amount":amount})

def total_expense():
    total=0
    for expence_amount in expense:
        total = total + expence_amount["Amount"]
    return total