import os
from datetime import datetime
from pay.credit_card import CreditCard
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY") or ""

class PaymentProcessor:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def _check_api_key(self) -> bool:
        return self.api_key == API_KEY

    def charge(self,card:CreditCard,amount: int) -> None:
        if not self.validate_card(card):
            raise ValueError("Invalid card")
        if not self._check_api_key():
            raise ValueError("Invalid API key")
        print(f"Charging card number {card.number} for ${amount/100:.2f}")

    def validate_card(self, card: CreditCard) -> bool:
        return luhn_checksum(card.number) and datetime(card.expiry_year,card.expiry_month, 1) > datetime.now()

def luhn_checksum( card_number: str) -> bool:
    checksum = sum(int(d) for d in card_number)
    return checksum % 2 == 0
