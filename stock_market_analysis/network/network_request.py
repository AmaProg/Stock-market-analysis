from urllib.request import urlopen

import certifi
import json

class NetworkRequest:
    
    #----- attribut class -----
    #

    # ----- properties -----
    @property
    def rate_limiting(self):
        return self._rate_limiting

    @rate_limiting.setter
    def rate_limiting(self, value):
        self._rate_limiting = value

    @property
    def nbr_request(self):
        return self._nbr_request

    @nbr_request.setter
    def nbr_request(self, value):
        self._nbr_request = value

    # -----  end properties -----

    # ----- methods -----
    def __init__ (self):
        self.rate_limiting = 0
        self.nbr_request = 0

    @staticmethod
    def send_request(url):
        response = None

        try:
            response = urlopen(url, cafile=certifi.where())
            
            data = response.read().decode("utf-8")

            return json.loads(data)

        except Exception as e:
            print(f'request network fail for {e}')

            return response
    # ----- end methods -----