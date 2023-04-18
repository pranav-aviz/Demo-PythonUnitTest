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
    order.line_items.append(LineItem(name="Item1", price=100, quantity=2))
    order.line_items.append(LineItem(name="Item2", price=50))
    assert order.total == 250
    
def test_order_total_multiple_items():
    order = Order()
    order.line_items.append(LineItem(name="Item1", price=100, quantity=2))
    order.line_items.append(LineItem(name="Item2", price=50))
    order.line_items.append(LineItem(name="Item3", price=25, quantity=3))
    assert order.total == 325

def test_order_pay():
    order = Order()
    order.pay()
    assert order.status == OrderStatus.PAID
    