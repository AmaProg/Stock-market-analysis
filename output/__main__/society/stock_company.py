import copy

from society.overview import Overview
from society.history_data import HistoryData
from society.financial_statement import FinancialStatement
from society.financial_ratio import FinancialRatio
from commun import utils

class Enterprise:
    
    def __init__(self) -> None:
        self.overview = Overview()
        self.history_data = HistoryData()
        self.financial_statement = FinancialStatement()
        self.financial_ratio = FinancialRatio(self.financial_statement)

    #-----  properties -----
    @property
    def company_name(self):
        return self.overview.get_company_name()

    @property
    def symbol(self):
        return self.overview.get_symbol()
    
    @property
    def share_price(self):
        return self.overview.get_share_price()
    
    @property
    def annual_dividend(self):
        return self.get_annual_dividend()
    
    @property
    def dividend_growth(self):
        return self.history_data.get_dividend_growth()
    
    @property
    def dividend_yield(self):
        return self.financial_ratio.get_decimal_dividend_yield() * 100
    
    @property
    def is_aristocrate(self):
        return self.history_data.is_aristocrate_dividend()
    
    @property
    def estimate_growth(self):
        return self.__get_company_estimate_growth()
    
    @property
    def estimate_performance(self):
        return self.get_estimate_performance()
    
    @property
    def distribution_profit(self):
        return self.get_distribution_profit()

    #-----  end properties -----

    #-----  methods -----
    def get_estimate_performance(self):
        eps_growth = self.financial_statement.eps_growth
        dividend_yield = self.dividend_yield
        
        sum = eps_growth + dividend_yield
        
        return sum
    
    def get_distribution_profit(self) -> float:
        annual_dividend: float = self.annual_dividend
        eps: float = self.financial_statement.eps
        
        dist = (annual_dividend / eps) * 100
        
        return dist
    
    def __get_company_estimate_growth(self) -> float:
        eps_growth: float = self.financial_statement.eps_growth
        dividend_growth: float = self.dividend_growth
        
        mean = (eps_growth + dividend_growth) / 2
        
        if(mean >= 10):
            mean = 10
            
        return mean
    
    def get_annual_dividend(self):
        decimal_dividend_yield = self.financial_ratio.get_decimal_dividend_yield()
        share_price = self.share_price
        
        annual_dividend = decimal_dividend_yield * share_price
        
        return annual_dividend
    
    def to_json(self,path:str) -> None:
        f"""
        La fonction {self.to_json} permet de sauvegarder les 
        informations de la societer en fichier format json 
        """
        data = {}

        data['profile'] = self.overview.profile
        data['historical_dividend'] = self.history_data.historical_dividend
        data['financial_ratio'] = self.financial_ratio.company_financial_ratio
        data['income_statement'] = self.financial_statement.income_statement.historical_income_statement

        utils.write_json_file(path, data)

    def load(self, path: str) -> None:
        f"""
        La fonction {self.load} permet de charger les donnes de 
        l'entreprise qui ont ete sauvegarder avant 
        """

        json_data = utils.read_json_file(path)

        self.overview.profile = json_data['profile']
        self.history_data.historical_dividend = json_data ['historical_dividend']
        self.financial_ratio.company_financial_ratio = json_data['financial_ratio']
        self.financial_statement.income_statement.historical_income_statement = json_data['income_statement']

    #----- end methods -----
    