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
    GROSS_PROFIT_MARGIN = 'grossProfitMarginTTM'
    NET_PROFIT_MARGIN =  'netProfitMarginTTM'
    
class FMPIncomeStatement(Enum):
    EPS = 'eps'
    DATE = 'date'
    NET_PROFIT = 'netIncome'
    GROSS_PROFIT = 'grossProfit'
    SELLING_GENERAL_AND_ADMIN_EXPENSES = 'sellingGeneralAndAdministrativeExpenses'
    RND = 'researchAndDevelopmentExpenses'
    OPERATING_INCOME = 'operatingIncome'
    INTEREST_EXPENSE = 'interestExpense'