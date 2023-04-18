from pay.order import LineItem, Order, OrderStatus

def test_order_default():
    order = Order()
    assert order.status == OrderStatus.OPEN
    assert order.total == 0

def test_order_total_single_item():
    order = Order()
    order.line_items.append(LineItem(name="Item1", price=100, quantity=1))
    assert order.total == 100
    
def test_order_total():
    order = Order()
    order.line_items.append(LineItem(name="Item1", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Item2", price=50_00))
    assert order.total == 250_00
    