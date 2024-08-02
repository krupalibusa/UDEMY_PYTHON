x = 20
b = "hello"
try:
    result = x / b
except ZeroDivisionError as err:
    print(err)
except:
    print("Error is ther in your program")
else:
    print(result)
finally:
    print("End of Program")