import unittest
from account import Account
from account_type import AccountType
from customer import Customer


class TestSort(unittest.TestCase):

    def test_BankChargePremiumLessThanAWeek(self):
        premium = AccountType(True)
        account = Account(premium, 5)
        self.assertEqual(account.bankCharge(), 14.5)

    def test_BankChargePremiumMoreThanAWeek(self):
        premium = AccountType(True)
        account = Account(premium, 9)
        self.assertEqual(account.bankCharge(), 16.5)

    def test_OverdraftFeePremium(self):
        premium = AccountType(True)
        account = Account(premium, 9)
        self.assertEqual(account.overdraftFee(), 0.10)

    def test_OverdraftFeeNotPremium(self):
        premium = AccountType(False)
        account = Account(premium, 9)
        self.assertEqual(account.overdraftFee(), 0.20)

    def test_PrintCustomer(self):
        premium = AccountType(False)
        account = Account(premium, 9)
        customer = Customer("test", "tt", "tt@mail.com", "INDIVIDUAL", account)
        account.customer = customer
        self.assertEqual(account.printCustomer(), "test tt@mail.com")

    def test_calculateDiscountOverWeight(self):
        premium = AccountType(False)
        account = Account(premium, 9)
        discount = account.calculateDiscount([[5, 100], [6, 200]], True)
        self.assertEqual(discount, -1)

    def test_calculateDiscount(self):
        premium = AccountType(False)
        account = Account(premium, 9)
        discount = account.calculateDiscount([[5, 50], [6, 40]], True)
        self.assertEqual(discount, -2)

    def test_calculateDiscountUnderWeight(self):
        premium = AccountType(True)
        account = Account(premium, 9)
        discount = account.calculateDiscount([[5, 50], [6, 50]], True)
        self.assertEqual(discount, 11)

if __name__ == '__main__':
    unittest.main()