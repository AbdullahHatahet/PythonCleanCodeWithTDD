# # from customer import Customer
# # from account_type import AccountType
import customer


def CONST_PREMIUM_FEE():
    return 0.10


def CONST_FEE():
    return 0.20


def CONST_LIMIT_DAY_TO_OVERDRAWN():
    return 7


def CONST_BANK_CHARGE_FOR_EACH_OVERDRAWN_DAY():
    return 1.0


def CONST_BANK_CHARGE_FOR_EACH_DAY():
    return 1.75


def CONST_INITIAL_BANK_CHARGE():
    return 4.5


def CONST_BANK_CHARGE_PREMIUM():
    return 10


def CONST_LIMIT_WEIGHT_ACCOUNT():
    return 100

class Account:
    # iban: str
    # type: # AccountType
    # days_overdrawn: int
    # money: float
    # currency: str
    # customer: Customer

    def __init__(self, account_type, days_overdrawn):
        self.account_type = account_type
        self.days_overdrawn = days_overdrawn
        self._customer = None
        self._money = None
        self._currency = None

    def bankCharge(self):
        bank_charge = CONST_INITIAL_BANK_CHARGE() + self.overdraftCharge()
        return bank_charge

    def overdraftCharge(self):
        if self.account_type.isPremium():
            return self.checkDays()
        else:
            return self.days_overdrawn * CONST_BANK_CHARGE_FOR_EACH_DAY()

    def checkDays(self):
        bank_charge_premium = CONST_BANK_CHARGE_PREMIUM()
        if self.checkOverdrawn():
            bank_charge_premium = CONST_BANK_CHARGE_PREMIUM() + (self.days_overdrawn - CONST_LIMIT_DAY_TO_OVERDRAWN())\
                                  * CONST_BANK_CHARGE_FOR_EACH_OVERDRAWN_DAY()
        return bank_charge_premium

    def checkOverdrawn(self):
        return self.days_overdrawn > CONST_LIMIT_DAY_TO_OVERDRAWN()

    def overdraftFee(self):
        if self.account_type.isPremium():
            return CONST_PREMIUM_FEE()
        else:
            return CONST_FEE()

    def printCustomer(self):
        return self.customer.name + " " + self.customer.email

    def amountSum(self, purchase_order_amounts):
        # TODO Implement this
        amount_sum = 0
        for i in range(len(purchase_order_amounts)):
            amount_sum += purchase_order_amounts[i][0]
        return amount_sum

    def amountWeightSum(self, purchase_order_amounts):
        # TODO Implement this
        weight_sum = 0
        for i in range(len(purchase_order_amounts)):
            weight_sum += purchase_order_amounts[i][1]
        return weight_sum

    def hasToIncreaseOneExtraPoint(self):
        # TODO Implement this
        return False

    def calculateDiscount(self, purchase_order_amounts, has_reached_minimum_amount):
        # TODO Implement this
        if not self.isEmpty(purchase_order_amounts):
            return self.checkAmountWeightSum(purchase_order_amounts, has_reached_minimum_amount)
        else:
            return 0

    def isEmpty(self, purchase_order_amounts):
        return purchase_order_amounts == []

    def checkAmountWeightSum(self, purchase_order_amounts, has_reached_minimum_amount):
        amount_sum = self.amountSum(purchase_order_amounts)
        amount_weight_sum = self.amountWeightSum(purchase_order_amounts)
        if amount_weight_sum == CONST_LIMIT_WEIGHT_ACCOUNT():
            return self.minimumAmount(has_reached_minimum_amount, amount_sum)
        elif amount_weight_sum > CONST_LIMIT_WEIGHT_ACCOUNT():
            return -1
        else:
            return -2

    def minimumAmount(self, has_reached_minimum_amount, amount_sum):
        if has_reached_minimum_amount:
            return self.extraPoint(amount_sum)
        else:
            return 0

    def extraPoint(self, amount_sum):
        if self.hasToIncreaseOneExtraPoint():
            return 10
        else:
            return amount_sum

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self._money = money

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        self._customer = customer

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency
