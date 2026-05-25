from strategy_payment import *
from observer_system import *

def main():
    print("=== Strategy Pattern ===\n")
    payment = PaymentContext(UPI())

    payment.make_payment(500)

    payment.set_strategy(CreditCard())

    payment.make_payment(1500)

    payment.set_strategy(PayPal())

    payment.make_payment(2500)

    print("\n=== Observer Pattern ===\n")
    event_manager = EventManager()

    user1 = UserSubscriber("Sushank")
    user2 = UserSubscriber("Rahul")
    user3 = UserSubscriber("Aman")

    event_manager.subscribe(user1)
    event_manager.subscribe(user2)
    event_manager.subscribe(user3)
    event_manager.notify("New Event Started!")

if __name__ == "__main__":
    main()