class IncomeStatement:
    @property
    def income_statement(self):
        return self._income_statement
    
    @income_statement.setter
    def income_statement(self, value):
        self._income_statement = value
        
    