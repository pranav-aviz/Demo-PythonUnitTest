from pay.order import LineItem

def test_line_item_default():
    item = LineItem(name="Test", price=100)
    assert item.quantity == 1

def test_line_item_total():
    item = LineItem(name="Test", price=100, quantity=2)
    assert item.total == 200
 