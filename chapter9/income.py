income = []

def add_income(amount,source):
    income.append({"Source":source,"Amount":amount})

def total_income():
    total=0
    for income_amount in income:
        total = total + income_amount["Amount"]
    return total