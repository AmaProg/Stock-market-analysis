from app.network_request import NetworkRequest

class Alpha_vantage:
    # ----- properties -----
    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value

    @property
    def network_request(self):
        return self._network_request

    @network_request.setter
    def network_request(self, value):
        self._network_request = value

    # ----- end properties -----

    # ----- methods -----
    def __init__(self):
        self.network_request = NetworkRequest()

    def get_income_statement(self, ticker, is_demo = False):
        value = None

        return value

    def get_balance_sheet(self, ticker, is_demo = False):
        value = None

        return value

    def get_cash_flow(self, ticker, is_demo = False):
        value = None

        return value

    def get_earning_history(self, ticker, is_demo = False):

        if (is_demo == True):
            url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={ticker}&apikey=demo'

        else:
            url = ''

        value = self.network_request.send_request(url)

        return value

    # ----- end methods -----