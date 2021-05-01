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
