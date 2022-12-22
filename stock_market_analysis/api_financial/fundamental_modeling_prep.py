from network_request import NetworkRequest
from enum import Enum

class FundamentalModelingPrep:
    
    #----- attribut class -----
    host_url = "https://financialmodelingprep.com"
    api_version = "api/v3"
    base_uri = "{}/{}".format(host_url,api_version)
    #----- end attribut class -----
    
    #----- constructor -----
    def __init__(self, api_key:str):
        self.api_key = api_key
    #----- end constructor -----
    
    
    #----- methods -----
    def get_profile(self, ticker:str):
        uri = "{}/{}/{}?apikey={}".format(self.base_uri, FMPRessource.PROFILE.value, ticker.upper(), self.api_key)
        
        json_data = NetworkRequest.send_request(uri)
        
        return json_data
    
    def get_historical_dividend(self, ticker:str):
        uri = "{}/{}/{}?apikey={}".format(self.base_uri, FMPRessource.HISTORICAL_DIVIDEND.value, ticker.upper(), self.api_key)
        
        json_data = NetworkRequest.send_request(uri)
        
        return json_data
    #----- end methods -----
    
class FMPRessource(Enum):
    PROFILE = "profile"
    HISTORICAL_DIVIDEND = "historical-price-full/stock_dividend"