

# Exceptions


class AuthenticationError(Exception):
    error_msg = '''
        Please make sure to initialize client_id and client_secret;

        Here an example;

        >>> from tigopesa import Tigopesa
        >>> tigopesa = Tigopesa(
                    client_secret='xxxx',
                    client_id ='xxxx'
                    environment="sandbox"
                )

        OR 

        You can do this;

        >>> from tigopesa import Tigopesa
        >>> tigopesa = Tigopesa(environment='production')
        >>> tigopesa.client_id = 'xxxx'
        >>> tigopesa.client_secret = "xxxx'
    '''

    def __init__(self, error_msg=error_msg) -> None:
        super().__init__(error_msg)


class ConfigurationError(Exception):
    error_msg = '''
    
    Missing account, pin, account_id !!!

    Please Make sure to configure tigopesa before calling this module
    
    do this to configure;

    >>> from tigopesa import Tigopesa
    >>> tigopesa.configure(
                account = '255xxxxx', 
                pin = 'xxxxx'
                account_id = 'xxxxxx'
                .........
            )

    '''

    def __init__(self, error_msg=error_msg) -> None:
        super().__init__(error_msg)
