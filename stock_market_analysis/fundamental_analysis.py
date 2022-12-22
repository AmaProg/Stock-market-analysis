import pandas as pd

from society.stock_company import Enterprise
from commun import constants as k

HEADER_ENTERPRISE = 'Entreprise'
HEADER_TICKER = 'Ticker'
HEADER_GROWTH_EPS = 'Croiss. BPA (%)'
HEADER_EPS = "BPA ($)"
HEADER_GROWTH_DIV = 'Croiss. Div (%)'
HEADER_ANNUAL_DIV = 'Div Annuel ($)'
HEADER_SHARE_PRICE = 'Prix action ($)'
HEADER_RENDEMENT = 'Rendement (%)'
HEADER_GROWTH_ESTIMATE = "Croiss. estimer (%)"
HEADER_NOTE = 'Performance (%)'
HEADER_DISTRIBUTION_INCOME = 'Distribution Profit (%)'
HEADER_DIVIDEND_ARISTOCRATS = 'Aristocrat dividend'

class FundamentalAnalysis:

    __ent: Enterprise = Enterprise()
    __table: dict = {
        HEADER_ENTERPRISE: 0,
        HEADER_TICKER: 0,
        HEADER_GROWTH_EPS: 0,
        HEADER_EPS: 0,
        HEADER_GROWTH_DIV: 0,
        HEADER_ANNUAL_DIV: 0,
        HEADER_SHARE_PRICE: 0,
        HEADER_RENDEMENT: 0,
        HEADER_GROWTH_ESTIMATE: 0,
        HEADER_NOTE: 0,
        HEADER_DISTRIBUTION_INCOME: 0,
        HEADER_DIVIDEND_ARISTOCRATS: 0
    }

    #----- constructor -----
    def __init__(self, ticker: list):
        self._ticker_list = ticker
        
    #----- end constructor -----

    #----- methods -----
    def build_dividend_strategy_table(self):

        enterprise_dict = self.__load_company_data()

        for ticker in enterprise_dict.keys():

            self.__ent: Enterprise = enterprise_dict[ticker]

            self.__table[HEADER_ENTERPRISE] = self.__ent.company_name
            self.__table[HEADER_TICKER] = self.__ent.symbol


    def __load_company_data(self) -> dict:

        enterprise_dict = {}

        for ticker in self._ticker_list:

            self.__ent.load(f"{k.DATA_PATH}/{ticker}.json")

            enterprise_dict[ticker] = self.__ent

            self.__ent = Enterprise()

        return enterprise_dict
        


    #----- end methods -----