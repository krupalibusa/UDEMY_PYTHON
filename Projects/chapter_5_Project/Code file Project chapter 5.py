# Simple Customer Service Chatbot
 
print("Welcome to the Customer Service Chatbot!")
 
print("How can I assist you today?")
print("1. Store Hours")
print("2. Return Policy")
print("3. Store address")
print("4. Troubleshooting")
 
# Getting user input
choice = input("Please enter the number of your choice: ")
 
# Handling user input with conditional statements
if choice == '1':
    print("Our store hours are:")
    print("Monday - Friday: 9 AM - 9 PM")
    print("Saturday: 10 AM - 6 PM")
    print("Sunday: Closed")
elif choice == '2':
    print("Return Policy:")
    print("You can return items within 30 days of purchase.")
    print("Items must be in original condition with receipt.")
elif choice == '3':
    print("Enter 1 for newyork")
    print("Enter 2 for marryland")
    city = input("Which city store addres you want?")
    if city =='1':
        print("20 Cooper Square, New York, NY 10003, USA")
    elif city == '2':
        print("55 Clark St, Brooklyn, Marryland 11201, USA")
    else:
        print("Invalid choice")
elif choice == '4':
    print("Troubleshooting:")
    print("For common issues, please visit our troubleshooting guide on our website.")
else:
    print("I'm sorry, I didn't understand that. Please try again.")
 
print("Thank you for using the Customer Service Chatbot!")
