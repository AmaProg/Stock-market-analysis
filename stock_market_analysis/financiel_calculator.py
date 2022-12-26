import pandas as pd

class FinancialCalculator:
    
    @staticmethod
    def calculate_multiplying_factor(start_value, arrival_value) -> float:
        """
        Le coefficient multiplicateur est un indicateur de comparaison
        pour mesurer le rapport entre deux variables, à savoir combien 
        de fois l'une est plus grande/petite que l'autre. Il se calcule
        ainsi : coefficient multiplicateur = valeur d'arrivée / valeur de départ
        """
        
        value = 0
        
        value = arrival_value / start_value
        
        return value
    
    @staticmethod    
    def overall_rate_of_change(data: dict):
        """
        Le coefficient multiplicateur global est égal au produit 
        des coefficients multiplicateurs successifs sur plusieurs 
        périodes. Il se calcule avec le coefficient multiplicateur
        global : (1+t1) x (1+t2) x …
        
        {orc}
        """
        
        value: float = 1
        
        df: pd.DataFrame = pd.DataFrame(data)
        df: pd.DataFrame = df.transpose()
        df: pd.DataFrame = df[::-1]
        df: pd.DataFrame = df.reset_index()
        
        
        number_element = len(df.index)
        mf: float = 1
        
        for i in range(0, number_element - 1):
            start_value = df['dividend'][i]
            arrival_value = df['dividend'][i+1]
            value *= FinancialCalculator.calculate_multiplying_factor(start_value, arrival_value)
            
        return value
    
    def calculate_average_annual_growth_rate(ocr, n):
        quot = 1 / n
        eq = pow(ocr, quot)
        
        value = (eq - 1) * 100
        
        return value