from pay.order import LineItem

def test_line_item_default():
    item = LineItem(name="Test", price=100)
    assert item.quantity == 1

def test_line_item_total():
    item = LineItem(name="Test", price=100, quantity=2)
    assert item.total == 200
 
def test_line_item_type():
    item = LineItem(name="Test", price=100)
    assert isinstance(item, LineItem)
    
def test_line_item_name():
    item = LineItem(name="Test", price=100)
    assert item.name == "Test"
