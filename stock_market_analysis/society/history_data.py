class HistoryData:
    
    @property
    def historical_dividend(self):
        return self._historical_dividend

    @historical_dividend.setter
    def historical_dividend(self, value):
        self._historical_dividend = value