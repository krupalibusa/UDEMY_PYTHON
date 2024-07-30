class Payment:
    def payment_method(self):
        pass

class UPI(Payment):
    def payment_method(self):
        print("Hi this is the payment method of UPI")

class CC(Payment):
    def payment_method(self):
        super().payment_method()
        print("This is the payment method of Credit card class")

credit_card = CC()
credit_card.payment_method()