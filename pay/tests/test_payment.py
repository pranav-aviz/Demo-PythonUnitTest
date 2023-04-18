from pay.payment import pay_order
from pay.order import LineItem, Order
from pytest import raises
from pay.credit_card import CreditCard
import pytest
from datetime import date

class PaymentProcessorMock:
    def charge(self, card: CreditCard, amount: int) -> None:
        print(f"Charging card number {card.number} for ${amount/100:.2f}")

@pytest.fixture
def card() -> CreditCard:
    future_year = date.today().year + 1
    return CreditCard("4242424242424242", 12, future_year)

def test_pay_order(card:CreditCard):
    order = Order()
    order.line_items.append(LineItem("Test", 1, 100))
    pay_order(order,card, PaymentProcessorMock())
    
def test_pay_order_invalid_card(card:CreditCard):
    with raises(ValueError):
        order = Order()
        pay_order(order,card,PaymentProcessorMock())