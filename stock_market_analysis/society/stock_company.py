from society.overview import Overview
from society.history_data import HistoryData
from society.financial_statement import FinancialStatement
from commun import utils

class Enterprise:
    overview = Overview()
    history_data = HistoryData()
    financial_statement = FinancialStatement()

    #-----  properties -----
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value
    #-----  end properties -----

    #-----  methods -----
    def to_json(self,path:str) -> None:
        f"""
        La fonction {self.to_json} permet de sauvegarder les 
        informations de la societer en fichier format json 
        """
        data = {}

        data['profile'] = self.overview.profile
        data['historical_dividend'] = self.history_data.historical_dividend

        utils.write_json_file(path, data)

    def load(self, path: str) -> None:
        f"""
        La fonction {self.load} permet de charger les donnes de 
        l'entreprise qui ont ete sauvegarder avant 
        """

        json_data = utils.read_json_file(path)

        self.overview.profile = json_data['profile']
        self.history_data.historical_dividend = json_data ['historical_dividend']

    #----- end methods -----
    