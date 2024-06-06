'''
ISP: Interface Segregation Principle (インターフェース分離の原則)
'''


class PaymentProcessor:
    def process_credit_card_payment(self, card_number, amount):
        print(f"Processing credit card payment for {amount} on card {card_number}")

    def process_paypal_payment(self, email, amount):
        print(f"Processing PayPal payment for {amount} on email {email}")


class Customer:
    def __init__(self, email, card_number):
        self.email = email
        self.card_number = card_number


class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items

    def make_payment(self, payment_processor):
        for item in self.items:
            if isinstance(item, DigitalItem):
                payment_processor.process_paypal_payment(self.customer.email, item.price)
            else:
                payment_processor.process_credit_card_payment(self.customer.card_number, item.price)


class Item:
    def __init__(self, price):
        self.price = price


class DigitalItem(Item):
    def __init__(self, price):
        super().__init__(price)


class PhysicalItem(Item):
    def __init__(self, price):
        super().__init__(price)


if __name__ == '__main__':
    payment_processor = PaymentProcessor()
    customer = Customer("test@hoge.com", "1111-2222-3333-4444")
    order = Order(customer, [DigitalItem(100), PhysicalItem(200)])
    order.make_payment(payment_processor)