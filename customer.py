class Customer:

    def __init__(self, name, surname, email, customer_type, account, company_overdraft_discount=1):
        self.name = name
        self.surname = surname
        self.email = email
        self._customer_type = customer_type
        self.account = account
        self.company_overdraft_discount = company_overdraft_discount

    @property
    def customer_type(self):
        return self._customer_type

    @customer_type.setter
    def customer_type(self, customer_type):
        self._customer_type = customer_type

    def withdraw(self, withdraw_money, currency):
        if not self.account.currency == currency:
            raise Exception("Can't extract withdraw " + currency)

        if self.isNotOverdraft():
            self.discount(withdraw_money)

        elif self.account.account_type.isPremium():
            self.groupOrIndividualPremiumAccount(withdraw_money)
        else:
            self.overdraft(withdraw_money)

    def isNotOverdraft(self):
        return self.account.money >= 0

    def overdraft(self, withdraw_money):
        self.account.money = self.accountMoneyAfterWithdrawWithoutFee(withdraw_money) - self.withdrawFee(withdraw_money)

    def groupOrIndividualPremiumAccount(self, withdraw_money):
        if self.customer_type == 'GROUP':
            self.discountFiftyPercentFee(withdraw_money)

        elif self.customer_type == 'INDIVIDUAL':
            self.overdraft(withdraw_money)

    def discountFiftyPercentFee(self, withdraw_money):
        self.account.money = self.accountMoneyAfterWithdrawWithoutFee(withdraw_money) - self.withdrawFee(withdraw_money) / 2

    def accountMoneyAfterWithdrawWithoutFee(self, withdraw_money):
        return self.account.money - withdraw_money

    def withdrawFee(self, withdraw_money):
        return withdraw_money * self.account.overdraftFee() * self.company_overdraft_discount

    def discount(self, withdraw_money):
        self.account.money = self.account.money - withdraw_money

    def printCustomerDaysOverdrawn(self):
        account_description = self.printCustomerIban() + ", Days Overdrawn: " + str(
            self.account.days_overdrawn)
        return self.printCustomerName() + account_description

    def printCustomerMoney(self):
        account_description = self.printCustomerIban() + ", Money: " + str(self.account.money)
        return self.printCustomerName() + account_description

    def printCustomerName(self):
        return str(self.name) + " " + str(self.surname) + " "

    def printCustomerIban(self):
        return "Account: IBAN: " + str(self.account.iban)

    def printCustomerAccount(self):
        return self.printCustomerIban() + self.printCustomerMoney() + ", Account type: " + self.printCustomerIsPremiumOrNormal()

    def printCustomerIsPremiumOrNormal(self):
        if self.account.account_type.isPremium():
            return "Premium"
        else:
            return "Normal"
