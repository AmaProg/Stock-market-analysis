from sma_enum.fmp_enum import FMPFinancialRatio
from society.financial_statement import FinancialStatement

class FinancialRatio:
    
    #----- constructor -----
    def __init__(self, financial_statement) -> None:
        self.company_financial_ratio = {}
        self.financial_statement: FinancialStatement = financial_statement
    #----- end constructor -----
    
    @property
    def company_financial_ratio(self):
        return self._company_financial_ratio
    
    @company_financial_ratio.setter
    def company_financial_ratio(self, value):
        self._company_financial_ratio = value
        
    @property
    def net_margin_TTM(self):
        return self.__get_financial_ratio_data(FMPFinancialRatio.NET_PROFIT_MARGIN.value)
    
    @property
    def gross_margin_TTM(self):
        return self.__get_financial_ratio_data(FMPFinancialRatio.GROSS_PROFIT_MARGIN.value)
        
    #----- methods -----
    def get_decimal_dividend_yield(self):
        return self.__get_financial_ratio_data(FMPFinancialRatio.DECIMAL_DIVIDEND_YIELD.value)
    
    #----- end methods ------
    
    #----- private methods -----
    def __get_financial_ratio_data(self, key):
        financial_ratio = self._company_financial_ratio[0]
        
        value = financial_ratio[key]
        
        return value
     #----- end private methods ------