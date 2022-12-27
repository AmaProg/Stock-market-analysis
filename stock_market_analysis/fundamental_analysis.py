import copy

from society.stock_company import Enterprise
from commun import constants as k, utils

HEADER_ENTERPRISE = 'Entreprise'
HEADER_TICKER = 'Ticker'
HEADER_EPS = "BPA ($)"
HEADER_GROWTH_EPS = 'Croiss. BPA (%)'
HEADER_ANNUAL_DIV = 'Div Annuel ($)'
HEADER_GROWTH_DIV = 'Croiss. Div (%)'
HEADER_SHARE_PRICE = 'Prix action ($)'
HEADER_RENDEMENT = 'Rendement (%)'
HEADER_GROWTH_ESTIMATE = "Croiss. estimer (%)"
HEADER_NOTE = 'Performance (%)'
HEADER_DISTRIBUTION_INCOME = 'Distribution Profit (%)'
HEADER_DIVIDEND_ARISTOCRATS = 'Aristocrat dividend (number reduce)'

class FundamentalAnalysis:
    
    #----- constructor -----
    def __init__(self, ticker: list):
        self._ticker_list = ticker
        self.__ent: Enterprise = None
        self.__table: None
        self.__column = {
            HEADER_ENTERPRISE: 0,
            HEADER_TICKER: 0,
            HEADER_EPS: 0,
            HEADER_GROWTH_EPS: 0,
            HEADER_ANNUAL_DIV: 0,
            HEADER_GROWTH_DIV: 0,
            HEADER_SHARE_PRICE: 0,
            HEADER_RENDEMENT: 0,
            HEADER_GROWTH_ESTIMATE: 0,
            HEADER_NOTE: 0,
            HEADER_DISTRIBUTION_INCOME: 0,
            HEADER_DIVIDEND_ARISTOCRATS: 0
        }   
    #----- end constructor -----

    #----- methods -----
    def build_dividend_strategy_table(self):

        enterprise_dict: dict = self.__load_company_data()
        value = []

        for ticker in enterprise_dict.keys():
            
            self.__table = copy.deepcopy(self.__column)

            enterprise: Enterprise = enterprise_dict[ticker]

            self.__table[HEADER_ENTERPRISE] = enterprise.company_name
            self.__table[HEADER_TICKER] = enterprise.symbol
            self.__table[HEADER_ANNUAL_DIV] = enterprise.annual_dividend
            self.__table[HEADER_SHARE_PRICE] = enterprise.share_price
            self.__table[HEADER_RENDEMENT] = enterprise.dividend_yield
            self.__table[HEADER_GROWTH_DIV] = enterprise.dividend_growth
            self.__table[HEADER_DIVIDEND_ARISTOCRATS] = enterprise.is_aristocrate
            self.__table[HEADER_EPS] = enterprise.financial_statement.eps
            self.__table[HEADER_GROWTH_EPS] = enterprise.financial_statement.eps_growth
            self.__table[HEADER_GROWTH_ESTIMATE] = enterprise.estimate_growth
            self.__table[HEADER_NOTE] = enterprise.estimate_performance
            self.__table[HEADER_DISTRIBUTION_INCOME] = enterprise.distribution_profit
            
            value.append(self.__table)
            
        utils.write_json_file(f"{k.DATABASE_SECTION_ANALYSIS}/dividend_analysis.json", value)


    def __load_company_data(self) -> dict:

        enterprise_dict = {}
            
        for ticker in self._ticker_list:
        
            enterprise_dict[ticker] = self.__get_enterprise_data(f"{k.TICKERS_PATH}/{ticker}.json")
            
        return enterprise_dict
        

    def __get_enterprise_data(self, json_file: str):
        
        self.__ent = Enterprise()
        
        self.__ent.load(json_file)
        
        return self.__ent
    #----- end methods -----