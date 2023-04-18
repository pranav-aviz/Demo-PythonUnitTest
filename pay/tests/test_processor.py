import pytest
from pay.processor import PaymentProcessor

API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"
VALID_CARD = "4242424242424242"

def test_valid_api_key():
    processor = PaymentProcessor(API_KEY)
    assert processor._check_api_key()

def test_api_key():
    processor = PaymentProcessor(API_KEY)
    assert processor.api_key == API_KEY

def test_empty_api_key():
    processor = PaymentProcessor("")
    assert not processor._check_api_key() 
    
def  test_card_valid_date():
    processor = PaymentProcessor(API_KEY)
    assert processor.validate_card(VALID_CARD, 12, 2023)
    
def test_card_invalid_date():
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge(VALID_CARD, 12, 2019,100)

def test_valid_checksum():
    processor = PaymentProcessor(API_KEY)
    assert processor.luhn_checksum(VALID_CARD)

def test_invalid_checksum():
    processor = PaymentProcessor(API_KEY)
    assert not processor.luhn_checksum("12345")
    
def test_charge():
    processor = PaymentProcessor(API_KEY)
    processor.charge(VALID_CARD, 12, 2023, 100)

def test_invalid_card():
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge("12345", 12, 2023, 100)