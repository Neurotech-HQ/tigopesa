from tigopesa.utils import urls
import requests
from typing import List, Dict, Union


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

    def get_headers(self) -> Dict:
        return {

        }