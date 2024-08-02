name = input("Enter Your name: ")
fund_amt = int(input("Enter fund amount: "))
try:
    if fund_amt < 500:
        raise ValueError("Fund amount should not be less than 500 ")    
    else:
        print("Thank for your time ")
except ValueError as err:
    print(err)