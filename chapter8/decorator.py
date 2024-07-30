def dec_fun(greet):
    def wrapper():
        print("hi all")
        greet()
        print("Bye all")
    return wrapper

@dec_fun
def greet():
    print("Hello")

greet()