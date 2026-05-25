class PaymentStrategy:
    def pay(self, amount):
        pass

class UPI(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class PayPal(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")

class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)