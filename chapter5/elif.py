distance = int(input("enter distacne of travelling "))
if(distance <= 5):
    print("go by walk")
elif(distance <= 10):
    print("go by cycle")
elif(distance <= 20):
    print("go by car")
else:
    print("go by flight")
