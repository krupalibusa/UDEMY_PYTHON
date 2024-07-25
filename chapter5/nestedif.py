
no1 = int(input("Enter number 1: ")) 
no2 = int(input("Enter number 2: ")) 
no3 = int(input("Enter number 3: ")) 
if (no1 > no2):
    if(no1 > no3):
        print("No 1 is max")
    else:
        print("No 3 is maximum number")
else:
    if(no2 > no3):
        print("No 2 is max")
    else:
        print("No 3 is maximum number")