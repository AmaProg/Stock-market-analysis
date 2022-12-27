import pandas as pd

from datetime import date
from financiel_calculator import FinancialCalculator

class IncomeStatement:
    @property
    def historical_income_statement(self):
        return self._historical_income_statement
    
    @historical_income_statement.setter
    def historical_income_statement(self, value):
        self._historical_income_statement = value
        
    def __get_eps_table(self) -> dict:
        """_summary_

        Returns:
            dict: _description_
        """
        
        historical_eps = self._historical_income_statement
        
        df = pd.DataFrame(historical_eps)
        eps_dict: dict = {}
        
        for index, row in df.iterrows():
            reporte_date: str = row['date']
            
            eps_dict[reporte_date[0:4]] = {'eps': row['eps']}
                
        return eps_dict
    
    def get_current_eps(self) -> float:
        """_summary_

        Returns:
            float: _description_
        """
        # current_year: int = date.today().year
        
        eps_dict: dict = self.__get_eps_table()
        
        first_value: dict = list(eps_dict.values())[0]
        
        eps = first_value['eps']
        
        # eps = 0
        # number_element = len(eps_dict)
        # is_present = False
        
        # for key in eps_dict.keys():
            
        #     for i in range(0, number_element):
            
        #         if(key == current_year-i):
        #             section: dict = eps_dict.get(key)
        #             eps = section.get('eps', 999)
        #             is_present = True
        #             break
                
        #     if(is_present == True):
        #         break
            
        return eps
    
    def get_eps_growth(self) -> float:
        """_summary_

        Returns:
            float: _description_
        """
        
        eps_dict: dict = self.__get_eps_table()
        
        orc = FinancialCalculator.overall_rate_of_change(eps_dict, 'eps')
        
        aagr = FinancialCalculator.calculate_average_annual_growth_rate(orc, len(eps_dict))
        
        return aagr
    
    