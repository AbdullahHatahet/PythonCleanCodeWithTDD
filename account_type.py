class AccountType:
    _premium: bool

    def __init__(self, premium):
        self._premium = premium

    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, premium):
        self._premium = premium

    def isPremium(self):
        return self._premium
