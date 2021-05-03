import uuid
from pydantic import BaseModel
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class urls(object):

    SANDBOX_BASE_URL = 'https://securesandbox.tigo.com'
    PRODUCTION_BASE_URL = 'https://secure.tigo.com'

    def __init__(self, enviro='production') -> None:
        self._enviro = enviro
        self.base_url = (self.PRODUCTION_BASE_URL
                         if enviro == 'production'
                         else self.SANDBOX_BASE_URL
                         )

        self.token_url = f'{self.base_url}//v1/oauth/generate/accesstoken?grant_type=client_credentials'
        self.authorize_payement_url = f'{self.base_url}//v1/tigo/payment-auth/authorize'

# using Pydantic for verification of data


class Config(BaseModel):

    # Master mechant

    account: str
    pin: str
    account_id: str

    # Mechant Informations

    mechant_reference: Optional[str] = ''
    mechant_fee: Optional[str] = '0.0'
    mechant_currency_code: Optional[str] = ''

    # Other_information
    language: Optional[str] = 'eng'
    terminal_id: Optional[str] = ''
    currency_code: Optional[str] = 'TZS'

    tax: Optional[str] = '0.0'
    fee: Optional[str] = '0.0'

    exchange_rate: Optional[str] = '1'

    # Callbacks and Redirects

    callback_url: Optional[str] = 'https://kalebujordan.dev/'
    redirect_url: Optional[str] = 'https://kalebu.github.io/pypesa/'

    # Subscribers default Information

    subscriber_country_code: Optional[str] = '255'
    subscriber_country: Optional[str] = 'TZA'

    @property
    def random_reference(self) -> str:
        return str(uuid.uuid4()).replace('-', '')


class secureCustomerPaymentData(BaseModel):
    # Required parameters

    amount: str
    first_name: str
    last_name: str
    customer_email: str
    mobile: str

    # Optional Parameters

    redirect_url: Optional[str]
    callback_url: Optional[str]
    country_code: Optional[str]
    country: Optional[str]
    language: Optional[str]
    terminal_id: Optional[str]
    from_currecy_code: Optional[str]
    to_currency_code: Optional[str]
    exchange_rate: Optional[str]
    exchanged_amount: Optional[str]
