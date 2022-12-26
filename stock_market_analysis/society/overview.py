from sma_enum.fmp_enum import FMPProfile, FMPHistoricalDividend

class Overview:
    
    @property
    def profile(self) -> dict:
        return self._profile

    @profile.setter
    def profile(self, value):
        self._profile: dict = value
        
    #----- methods -----
    def get_company_name(self):
        
        return self.__get_profile_data(FMPProfile.COMPANY_NAME.value)
    
    def get_symbol(self):
        
        return self.__get_profile_data(FMPProfile.SYMBOL.value)
    
    def get_share_price(self):
        return self.__get_profile_data(FMPProfile.SHARE_PRICE.value)
    
    def get_dividend_yield(self):
        return self.__get_profile_data(FMPProfile.DIVIDEND_YIELD.value)
        
    
    def __get_profile_data(self, key):
        
        profile = self._profile[0]
        
        value = profile[key]
        
        return value
        
        
    #----- end methods -----