import pandas as pd

from financiel_calculator import FinancialCalculator
from datetime import date
from sma_enum.fmp_enum import FMPHistoricalDividend

class HistoryData:
    
    @property
    def historical_dividend(self):
        return self._historical_dividend

    @historical_dividend.setter
    def historical_dividend(self, value):
        
        self._historical_dividend = value
        
    def __get_historical_dividend_list(self):
        return self._historical_dividend['historical']
    
    def to_dataframe(self, data) -> pd.DataFrame:
        return pd.DataFrame(data)
    
    def get_historical_dividend(self):
        return self.to_dataframe()
    
    def __get_historical_dividend_by_year(self) -> dict:
        #recuperer la liste des history des dividend
        historical_dividend: pd.DataFrame = self.to_dataframe(self.__get_historical_dividend_list())

        today = date.today()
        current_year = today.year
        pos = 0
        dividend_sum = 0
        dividend_data = {}
        
        for index, row in historical_dividend.iterrows():
            report_date: str = str(row['date'])
            last_year = current_year - pos
            
            if (report_date.find(str(last_year)) >= 0):
                dividend_sum += row[FMPHistoricalDividend.DIVIDEND_AJUSTED.value]
            else:
                dividend_data[last_year] = {"dividend":dividend_sum}
                dividend_sum = row[FMPHistoricalDividend.DIVIDEND_AJUSTED.value]
                pos += 1
                
        return dividend_data
    
    def get_dividend_growth(self):
        
        dividend_dict = self.__get_historical_dividend_by_year()
        
        orc = FinancialCalculator.overall_rate_of_change(dividend_dict, 'dividend')
                
        value = FinancialCalculator.calculate_average_annual_growth_rate(orc, len(dividend_dict))        
            
        return value
    
    def is_aristocrate_dividend(self):
        """_summary_
        """
        
        dividend_dict = self.__get_historical_dividend_by_year()
        
        df = pd.DataFrame(dividend_dict)
        df: pd.DataFrame = df.transpose()
        df: pd.DataFrame = df[::-1]
        df: pd.DataFrame = df.reset_index()
        
        number_element = len(df.index)
        value = 1
        number_dividend_reduce = 0
        is_aristocrate = True
        
        for i in range(0, number_element - 1):
            start_value = df['dividend'][i]
            arrival_value = df['dividend'][i+1]
            value = FinancialCalculator.calculate_multiplying_factor(start_value, arrival_value)
            
            if(value < 1):
                number_dividend_reduce += 1
            
        return number_dividend_reduce
                
        
        
        