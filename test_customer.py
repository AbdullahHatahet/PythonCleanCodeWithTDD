import unittest

from account import Account
from account_type import AccountType
from customer import Customer


class TestSort(unittest.TestCase):
    def test_WithdrawIndividualWithNormalAccount(self):
        premium = AccountType(False)
        account = Account(premium, 9)
        customer = Customer("test", "tt", "tt@mail.com", "INDIVIDUAL", account)
        account.customer = customer
        account.iban = "RO023INGB434321431241"
        account.money = 34.0
        account.currency = "EUR"
        customer.withdraw(10, "EUR")
        self.assertEqual(account.money, 24.0)

    def test_WithdrawIndividualWithNormalAccountAndOverdraft(self):
        premium = AccountType(False)
        account = Account(premium, 9)
        customer = Customer("test", "tt", "tt@mail.com", "INDIVIDUAL", account)
        account.customer = customer
        account.iban = "RO023INGB434321431241"
        account.money = -10.0
        account.currency = "EUR"
        customer.withdraw(10, "EUR")
        self.assertEqual(account.money, -22.0)

    def test_WithdrawIndividualWithPremiumAccount(self):
        premium = AccountType(True)
        account = Account(premium, 9)
        customer = Customer("test", "tt", "tt@mail.com", "INDIVIDUAL", account)
        account.customer = customer
        account.iban = "RO023INGB434321431241"
        account.money = 34.0
        account.currency = "EUR"
        customer.withdraw(10, "EUR")
        self.assertEqual(account.money, 24.0)

    def test_WithdrawIndividualWithPremiumAccountAndOverdraft(self):
        premium = AccountType(True)
        account = Account(premium, 9)
        customer = Customer("test", "tt", "tt@mail.com", "INDIVIDUAL", account)
        account.customer = customer
        account.iban = "RO023INGB434321431241"
        account.money = -10.0
        account.currency = "EUR"
        customer.withdraw(10, "EUR")
        self.assertEqual(account.money, -21.0)

    def test_WithdrawGroupWithNormalAccount(self):
        premium = AccountType(True)
        account = Account(premium, 9)
        customer = Customer("test", "tt", "tt@mail.com", "GROUP", account, 0.10)
        account.customer = customer
        account.iban = "RO023INGB434321431241"
        account.money = 34.0
        account.currency = "EUR"
        customer.withdraw(10, "EUR")
        self.assertEqual(account.money, 24.0)

    def test_WithdrawGroupWithNormalAccountAndOverdraft(self):
        premium = AccountType(False)
        account = Account(premium, 9)
        customer = Customer("test", "tt", "tt@mail.com", "GROUP", account, 0.50)
        account.customer = customer
        account.iban = "RO023INGB434321431241"
        account.money = -10.0
        account.currency = "EUR"
        customer.withdraw(10, "EUR")
        self.assertEqual(account.money, -21.0)

    def test_WithdrawGroupWithPremiumAccount(self):
        premium = AccountType(True)
        account = Account(premium, 9)
        customer = Customer("test", "tt", "tt@mail.com", "GROUP", account, 0.50)
        account.customer = customer
        account.iban = "RO023INGB434321431241"
        account.money = 34.0
        account.currency = "EUR"
        customer.withdraw(10, "EUR")
        self.assertEqual(account.money, 24.0)

    def test_WithdrawGroupWithPremiumAccountAndOverdraft(self):
        premium = AccountType(True)
        account = Account(premium, 9)
        customer = Customer("test", "tt", "tt@mail.com", "GROUP", account, 0.50)
        account.customer = customer
        account.iban = "RO023INGB434321431241"
        account.money = -10.0
        account.currency = "EUR"
        customer.withdraw(10, "EUR")
        self.assertEqual(account.money, -20.25)

    def test_PrintCustomerDaysOverdrawn(self):
        premium = AccountType(False)
        account = Account(premium, 10)
        customer = Customer("test", "tt", "tt@mail.com", "INDIVIDUAL", account)
        account.customer = customer
        account.iban = "RO023INGB434321431241"
        account.money = 34.0
        account.currency = "EUR"
        customer.withdraw(10, "EUR")
        self.assertEqual(customer.printCustomerDaysOverdrawn(),
                         "test tt Account: IBAN: RO023INGB434321431241, Days Overdrawn: 10")

    def test_PrintCustomerMoney(self):
        premium = AccountType(True)
        account = Account(premium, 10)
        customer = Customer("test", "tt", "tt@mail.com", "INDIVIDUAL", account)
        account.customer = customer
        account.iban = "RO023434321431241"
        account.money = 34.0
        account.currency = "EUR"
        customer.withdraw(10, "EUR")
        self.assertEqual(customer.printCustomerMoney(),
                         "test tt Account: IBAN: RO023434321431241, Money: 24.0")

    def test_PrintCustomerAccountNormal(self):
        premium = AccountType(False)
        account = Account(premium, 10)
        customer = Customer("test", "tt", "tt@mail.com", "INDIVIDUAL", account)
        account.customer = customer
        account.iban = "RO023434321431241"
        account.money = 34.0
        account.currency = "EUR"
        customer.withdraw(10, "EUR")
        self.assertEqual(customer.printCustomerAccount(),
                         "Account: IBAN: RO023434321431241test tt Account: IBAN: RO023434321431241,"
                         " Money: 24.0, Account type: Normal")

    def test_PrintCustomerAccountPremium(self):
        premium = AccountType(True)
        account = Account(premium, 10)
        customer = Customer("test", "tt", "tt@mail.com", "INDIVIDUAL", account)
        account.customer = customer
        account.iban = "RO023434321431241"
        account.money = 34.0
        account.currency = "EUR"
        customer.withdraw(10, "EUR")
        self.assertEqual(customer.printCustomerAccount(),
                         "Account: IBAN: RO023434321431241test tt Account: IBAN: RO023434321431241,"
                         " Money: 24.0, Account type: Premium")

    def test_Currency(self):
        premium = AccountType(True)
        account = Account(premium, 10)
        customer = Customer("test", "tt", "tt@mail.com", "INDIVIDUAL", account)
        account.customer = customer
        account.iban = "RO023434321431241"
        account.money = 34.0
        account.currency = "DOLLAR"
        self.assertRaises(Exception, customer.withdraw, 10, "EUR")

if __name__ == '__main__':
    unittest.main()
