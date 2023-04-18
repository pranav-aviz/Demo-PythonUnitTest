from pay.payment import pay_order
from pay.processor import PaymentProcessor
from pay.order import LineItem, Order
from pytest import MonkeyPatch, raises

def test_pay_order(monkeypatch:MonkeyPatch):
    def charge_mock(self: PaymentProcessor, card: str, month: int, year: int, amount: int):
        pass
    inputs = ["4242424242424242", "12", "2023"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr(PaymentProcessor,"_check_api_key", lambda _: True )
    monkeypatch.setattr(PaymentProcessor,"charge", charge_mock)
    order = Order()
    order.line_items.append(LineItem("Test", 1, 100))
    pay_order(order)
    
def test_pay_order_invalid_card(monkeypatch:MonkeyPatch):
    with raises(ValueError):
        inputs = ["4242424242424241", "12", "2023"]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        monkeypatch.setattr(PaymentProcessor,"_check_api_key", lambda _: True )
        order = Order()
        pay_order(order)