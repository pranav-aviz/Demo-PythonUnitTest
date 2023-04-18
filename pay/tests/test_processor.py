import pytest
import os
from datetime import date
from pay.processor import PaymentProcessor, luhn_checksum
from pay.credit_card import CreditCard
from datetime import date
from dotenv import load_dotenv

load_dotenv()
FUTURE_YEAR = date.today().year + 1
API_KEY = os.getenv("API_KEY") or "" 
VALID_CARD_NUMBER = "4242424242424242"
# reminder : valid card number will be any even number

@pytest.fixture
def card() -> CreditCard:
    future_year = date.today().year + 1
    return CreditCard(VALID_CARD_NUMBER, 12, future_year)

@pytest.fixture
def payment_processor() -> PaymentProcessor:
    return PaymentProcessor(API_KEY)

def test_valid_api_key(payment_processor:PaymentProcessor):
    assert payment_processor._check_api_key()

def test_api_key(payment_processor:PaymentProcessor):
    assert payment_processor.api_key == API_KEY

def test_empty_api_key(card:CreditCard):
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor("")
        payment_processor.charge(card, 100)
    
def  test_card_valid_date(card:CreditCard,payment_processor:PaymentProcessor):
    assert payment_processor.validate_card(card)
    
def test_card_invalid_date(payment_processor:PaymentProcessor):
    with pytest.raises(ValueError):
        payment_processor.charge(CreditCard(VALID_CARD_NUMBER,12,2000), 100)

def test_valid_checksum():
    assert luhn_checksum(VALID_CARD_NUMBER)

def test_invalid_checksum():
    assert not luhn_checksum("4242424242424243")
    
def test_charge(card:CreditCard,payment_processor:PaymentProcessor):
    payment_processor.charge(card, 100)

def test_invalid_card_NUMBER(payment_processor:PaymentProcessor):
    with pytest.raises(ValueError):
        payment_processor.charge(CreditCard("4242424242424243",12,FUTURE_YEAR), 100)