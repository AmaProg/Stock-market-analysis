class Overview:
    
    @property
    def profile(self) -> dict:
        return self._profile

    @profile.setter
    def profile(self, value):
        self._profile = value