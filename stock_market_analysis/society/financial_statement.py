from society.income_statement import IncomeStatement
from society.balance_sheet import BalanceSheet
from society.cash_flow import CashFlow

class FinancialStatement:
    
    #----- propeties -----
    @property
    def eps(self):
        return self.income_statement.get_current_eps()
    
    @property
    def eps_growth(self):
        return self.income_statement.get_eps_growth()
    #----- end properties -----
    
    
    #----- constructor -----
    def __init__(self) -> None:
        self.income_statement: IncomeStatement = IncomeStatement()
        self.balance_sheet = BalanceSheet()
        self.cash_flow = CashFlow()
    #----- end constructor
    
    