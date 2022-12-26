from enum import Enum

class FMPProfile(Enum):
    SYMBOL = "symbol"
    SHARE_PRICE = "price"
    COMPANY_NAME = "companyName"
    DIVIDEND_YIELD = "lastDiv"
    MARKET_CAPITALISATION = "mktCap"
    SECTOR = "sector"
    
class FMPHistoricalDividend(Enum):
    DATE = "date"
    DIVIDEND_AJUSTED = "adjDividend"
    DIVIDEND = 'dividend'
    
class FMPFinancialRatio(Enum):
    DECIMAL_DIVIDEND_YIELD = "dividendYielTTM"