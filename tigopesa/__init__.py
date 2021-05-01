import requests
from functools import wraps
from typing import List, Dict, Union
from requests.exceptions import ConnectTimeout
from tigopesa.utils import urls, Config, secureCustomerPaymentData
from tigopesa.exceptions import AuthenticationError, ConfigurationError


class Tigopesa(object):
    def __init__(self,
                 client_id: str = None,
                 client_secret: str = None,
                 callback_url: str = None,
                 environment: str = 'production'):

        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__callback_url = callback_url
        self.urls = urls(environment)
        self.enviro_types = ['production', 'sandbox']
        self.config = None

    @property
    def client_id(self) -> str:
        """client_id [summary]

        Returns:
            str: [client_id]
        """
        return self.__client_id

    @client_id.setter
    def client_id(self, client_id: str):
        """Set a new client_id [summary]

        Args:
            client_id (str): [description]
        """

        if not isinstance(client_id, str):
            raise TypeError(
                f'client_id should be of type<str> not {type(client_id)}')
        self.__client_id = client_id

    @property
    def client_secret(self) -> str:
        """Returns client_secret [summary]

        Returns:
            str: [description]
        """
        return self.__client_secret

    @client_secret.setter
    def client_secret(self, client_secret: str):
        """ Set a new client_secret [summary]

        Args:
            client_secret ([str]): [description]
        """

        if not isinstance(client_secret, str):
            raise TypeError(
                f'client_secret should be of type<str> not {type(client_secret)}')
        self.__client_secret = client_secret

    @property
    def callback_url(self) -> str:
        """callback_url [summary]

        Returns:
            str: [current callback url]
        """
        return self.__callback_url

    @callback_url.setter
    def callback_url(self, callaback_url: str):
        """ set a new callback_url [summary]

        Args:
            callaback_url (str): [description]
        """
        if not isinstance(callaback_url, str):
            raise TypeError(
                f'callback_url should be of type<str> not {type(callaback_url)}')
        self.__callback_url = callaback_url

    @property
    def access_token(self):
        try:
            return requests.post(
                self.urls.token_url,
                data={
                    'client_id': self.client_id,
                    'client_secret': self.client_secret
                },
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            ).json()
        except (requests.ConnectionError, requests.Timeout):
            raise ConnectionError(
                'Connection refused, check your internet connection')

    @property
    def enviro(self) -> str:
        """current environment

        Returns:
            str: [description]
        """

        return self.urls._enviro

    @enviro.setter
    def enviro(self, enviro: str):
        """
        set a new environment 

        Args:
            enviro (str): [description]
        """

        if not isinstance(enviro, str):
            raise TypeError(
                f'enviro should be a of type<str> not <{type(enviro)}')

        if enviro.lower() not in self.enviro_types:
            raise ValueError(
                f'enviro should either be production or sandbox not {enviro}')

        self.urls = urls(enviro)

    def configure(self, **params):
        self.config = Config(**params)
        return self.config

    def secured(target_method):
        @wraps(target_method)
        def verify_security(self, *args, **kwargs):
            if not self.client_secret or not self.client_id:
                raise AuthenticationError
            if not self.config:
                raise ConfigurationError
            return target_method(self, *args, **kwargs)
        return verify_security

    @secured
    def authorize_payment(self, transaction_query: Dict):
        verified_params = secureCustomerPaymentData(**transaction_query).dict()
        verified_params = {key: value for key,
                           value in verified_params.items() if value}
        # print(verified_params)
        r_body = self.__customer_payment_json(verified_params)
        # print(r_body)
        try:
            return requests.post(
                self.urls.authorize_payement_url,
                json=r_body,
                headers=self.headers
            ).json()
        except (requests.ConnectionError, ConnectTimeout):
            raise ConnectionError(
                "Failed to authorize your payment, check your internet connection")

    def __customer_payment_json(self, params: Dict) -> Dict:
        return {
            "MasterMerchant": {
                "account": self.config.account,
                "pin": self.config.pin,
                "id": self.config.account_id
            },
            "Merchant": {
                "reference": self.config.mechant_reference,
                "fee": self.config.mechant_fee,
                "currencyCode": self.config.currency_code
            },
            "Subscriber": {
                "account": params.get('mobile'),
                "countryCode": params.get('country_code', self.config.subscriber_country_code),
                "country": params.get('country', self.config.subscriber_country),
                "firstName": params.get('first_name'),
                "lastName": params.get('last_name'),
                "emailId": params.get('customer_email')
            },
            "redirectUri": params.get('redirect_url', self.config.redirect_url),
            "callbackUri": params.get('callback_url', self.config.callback_url),
            "language": params.get('language', self.config.language),
            "terminalId": params.get('terminal_id', self.config.terminal_id),
            "originPayment": {
                "amount": params.get('amount'),
                "currencyCode": params.get('currency_code', self.config.currency_code),
                "tax": params.get('tax', self.config.tax),
                "fee": params.get('fee', self.config.fee)
            },
            "exchangeRate": params.get('exchange_rate', self.config.exchange_rate),
            "LocalPayment": {
                "amount": params.get('exchanged_amount', params.get("amount")),
                "currencyCode": params.get('currecy_code', self.config.currency_code)
            },
            "transactionRefId": self.config.random_reference
        }

    @property
    def headers(self) -> Dict:
        return {
            'Content-Type': 'application/json',
            'accessToken': self.access_token.get('accessToken')
        }
