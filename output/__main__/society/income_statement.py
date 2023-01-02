import pandas as pd

from sma_enum.fmp_enum import FMPIncomeStatement 
from financiel_calculator import FinancialCalculator
from dictionary import Dictionary

class IncomeStatement:
    #----- properties -----
    @property
    def sae_per_gross_profit(self):
        return self._get_sae_per_gross_profit()
    
    @property
    def rnd_per_gross_profit(self):
        return self._get_rnd_per_gross_profit()
    
    @property
    def interest_expense_per_operating_income(self):
        return self._get_interest_expense_per_operating_income()
    
    @property
    def historical_income_statement(self):
        return self._historical_income_statement
    
    @historical_income_statement.setter
    def historical_income_statement(self, value):
        self._historical_income_statement = value
        
    @property
    def historical_net_profit(self) -> dict:
        return self.__get_net_profit_table()
    
    @property
    def historical_gross_profit(self) -> dict:
        return self.__get_gross_profit_table()
    
    @property
    def historical_selling_general_and_admin_expense(self) -> dict:
        return self.__get_selling_general_and_admin_expense_table()
    @property
    def historical_sae_per_gross_profit(self) -> dict:
        return self.__get_sae_per_gross_profit_table()
    
    @property
    def historical_rnd(self) -> dict:
        return self.__get_rnd_table()
    
    @property
    def historical_rnd_per_gross_profit(self):
        return self.__get_rnd_per_gross_profit()
    
    @property
    def historical_operating_income(self):
        return self.__get_operating_income_table()
    
    @property
    def historical_interest_expense(self):
        return self.__get_interest_expense_table()
        
    @property
    def historical_interest_expense_per_operating_income(self):
        return self.__get_interest_expense_per_operating_income()
    #----- end properties -----
    
    #----- methods -----
    def _get_sae_per_gross_profit(self):
        dictionary: Dictionary = Dictionary
        historical_sae_per_gross_profit = self.historical_sae_per_gross_profit
        
        return dictionary.first_value(historical_sae_per_gross_profit)
    
    def _get_rnd_per_gross_profit(self):
        dictionary: Dictionary = Dictionary
        historical_rnd_per_gross_profit = self.historical_rnd_per_gross_profit
        
        return dictionary.first_value(historical_rnd_per_gross_profit)
    
    def _get_interest_expense_per_operating_income(self):
        dictionary: Dictionary = Dictionary
        historical_ie_per_oi = self.historical_interest_expense_per_operating_income
        
        return dictionary.first_value(historical_ie_per_oi)
    
    def get_current_eps(self) -> float:
        """_summary_

        Returns:
            float: _description_
        """
        eps_dict : Dictionary = Dictionary()
        
        first_value: dict = eps_dict.first_value(self.__get_eps_table())
        
        eps = first_value['eps']
            
        return eps
    
    def get_eps_growth(self) -> float:
        """_summary_

        Returns:
            float: _description_
        """
        
        eps_dict: dict = self.__get_eps_table()
        
        orc = FinancialCalculator.overall_rate_of_change(eps_dict, FMPIncomeStatement.EPS.value)
        
        aagr = FinancialCalculator.calculate_average_annual_growth_rate(orc, len(eps_dict))
        
        return aagr
    
    def get_net_profit_growth(self):
        """_summary_
        """
        
        net_profit_dict: dict = self.historical_net_profit
        
        orc = FinancialCalculator.overall_rate_of_change(net_profit_dict,'net_profit')
        
        aagr = FinancialCalculator.calculate_average_annual_growth_rate(orc, len(net_profit_dict))
        
        return aagr
    
    def get_net_revenue(self) -> float:
        """
            La fonction {get_net_revenue} permet de recuperer le 
            revenue net de l'entreprise
        """
    
    def get_gross_profit_TTM(self) -> float:
        """
            La fonction get_gross_revenue permet de recupere le revenue 
            brut de l'entreprise

        Returns:
            float: _description_
        """
    
    def get_turnover(self):
        """
            La fonction {get_turnover} permet de recuperer le chiffre 
            d'affaire de l'entreprise
        """
    #----- end methods -----
    
    #----- private methods -----
    def __get_net_profit_table(self):
        return self.__build_dictionary_from_income_statement('net_profit', FMPIncomeStatement.NET_PROFIT.value)
    
    def __build_dictionary_from_income_statement(self, key: str, income_statement_key):
        """
            build_dictionary_from_income_statement permet de construire 
            un histories de donnes en fonction des information present dans le income statement

        Args:
            key (str): key est la cle qui sera utiliser pour identifier les donnes recuperer
            
            income_statement_key (any): income_statement_key
            est la cle du dictionnaire present dans le dictionnaire
            de income staement qui vient de l'API de Fundamental modeling prep
        """ 
        historical_eps = self._historical_income_statement
        
        df = pd.DataFrame(historical_eps)
        eps_dict: dict = {}
        
        for index, row in df.iterrows():
            reporte_date: str = row[FMPIncomeStatement.DATE.value]
            
            eps_dict[reporte_date[0:4]] = {key: row[income_statement_key]}
                
        return eps_dict
    
    def __get_eps_table(self) -> dict:
        """_summary_

        Returns:
            dict: _description_
        """
        return self.__build_dictionary_from_income_statement('eps',FMPIncomeStatement.EPS.value)
        
        # historical_eps = self._historical_income_statement
        
        # df = pd.DataFrame(historical_eps)
        # eps_dict: dict = {}
        
        # for index, row in df.iterrows():
        #     reporte_date: str = row[FMPIncomeStatement.DATE.value]
            
        #     eps_dict[reporte_date[0:4]] = {'eps': row[FMPIncomeStatement.EPS.value]}
                
        # return eps_dict
    
    def __get_gross_profit_table(self) -> dict:
        return self.__build_dictionary_from_income_statement('gross_profit',FMPIncomeStatement.GROSS_PROFIT.value)
    
    def __get_selling_general_and_admin_expense_table(self) -> dict:
        return self.__build_dictionary_from_income_statement('sae', FMPIncomeStatement.SELLING_GENERAL_AND_ADMIN_EXPENSES.value)
    
    def __get_rnd_table(self) -> dict:
        return self.__build_dictionary_from_income_statement('rnd',FMPIncomeStatement.RND.value)
    
    def __get_operating_income_table(self) -> dict:
        return self.__build_dictionary_from_income_statement('operating_income', FMPIncomeStatement.OPERATING_INCOME.value)
    
    def __get_interest_expense_table(self) -> dict:
        return self.__build_dictionary_from_income_statement('interest_expense', FMPIncomeStatement.INTEREST_EXPENSE.value)
    
    def __calculate_dict(self, dict_a: dict, dict_b: dict, key_a, key_b) -> dict:
        value = {}
        
        for key in dict_a.keys():
            dict_data_a: dict = dict_a[key]
            dict_data_b: dict = dict_b[key]
            
            data_a= dict_data_a.get(key_a)
            data_b = dict_data_b.get(key_b)
            
            if(data_b == 0):
                value[key] = "Non Applicable"
            else:
                value[key] = data_a / data_b
            
        return value
    
    def __get_sae_per_gross_profit_table(self):
        historical_sae =  self.historical_selling_general_and_admin_expense
        historical_gross_profit =  self.historical_gross_profit
              
        return self.__calculate_dict(historical_sae,historical_gross_profit,'sae','gross_profit')
            
    def __get_rnd_per_gross_profit(self):
        historical_rnd = self.historical_rnd
        historical_gross_profit = self.historical_gross_profit
        
        return self.__calculate_dict(historical_rnd, historical_gross_profit, 'rnd', 'gross_profit')
    
    def __get_interest_expense_per_operating_income(self):
        historical_ie = self.historical_interest_expense
        historical_oi = self.historical_operating_income
        
        return self.__calculate_dict(historical_ie, historical_oi, 'interest_expense', 'operating_income')
            
    #----- end private methods -----
    