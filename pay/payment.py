from asyncio import Protocol
from pay.order import Order
from pay.credit_card import CreditCard
from pay.processor import PaymentProcessor

class PaymentProcessor(Protocol):
    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        """"charges the card for the given amount."""

def pay_order(order: Order,card: CreditCard, payment_processor:PaymentProcessor):
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    payment_processor.charge(card, amount=order.total)
    order.pay()
