"""
Toll contains python function for calculating money
"""
from typing import List


class MoneyError(BaseException):
    """
    Error called when money is not an instance of Money
    """
    pass


class Money:
    """
    Class for Money. During init, amount must be in cents.
    """

    def __init__(self, amount: int):
        if type(amount) != int:
            raise TypeError(f"Type {type(amount)} is invalid")
        self.cents = str(amount) + "¢"
        if int(self.cents[:-1]) < 1:
            raise SyntaxError("Cents is less than 1")
        else:
            self.money = "$" + str(round(int(self.cents[:-1]) / 100, 2))

    def __str__(self):
        return self.money

    def centsValue(self):
        """
        Return the value in cents
        """
        return self.cents

    def moneyValue(self):
        """
        Return the value in money
        """
        return self.money


def fixedintrest(money: Money, years: int, percentage: int or float, showmoney: bool = True, decimalplaces: int = 2) -> int:
    """
    Returns the fixed intrest. Years how long the fixed bank intrest has been given and percentage is the intrest each year.

    money
    =====
    The money, should be an instance of class Money

    years
    =====
    How long the money has been inside the bank

    percentage
    ==========
    The percentage of money that will be given each year

    showmoney
    =========
    A boolean to show if to display in cents or money, default is True

    decimalplaces
    =============
    The decimalplaces to show when rounding off, defualt is 2

    Example
    =======
    >>> from coconut.toll import Money, fixedintrest
    >>> m = Money(10) #10¢
    >>> fixedintrest(m, 2, 10, True, 2)
    '$0.12'
    >>> fixedintrest(m, 3, 50, False, 2)
    '25¢'
    """
    if type(decimalplaces) != int:
        raise TypeError(f"decimalplaces cannot be {type(decimalplaces)}! Can only be integer")
    elif type(showmoney) != bool:
        raise TypeError(f"showmoney cannoot be {type(showmoney)}! Can only be bool")
    elif type(percentage) not in [int, float]:
        raise TypeError(f"percentage cannot be {type(percentage)}! Can only be integer or float")
    elif type(years) not in [int, float]:
        raise TypeError(f"years cannot be {type(years)}! Can only be integer")
    elif not isinstance(money, Money):
        raise MoneyError(f"money is not an instance if Money")
    else:
        if showmoney == None:
            raise ValueError("showmoney cannot be a None")
        else:
            percentage = percentage / 100
            years = int(years)
            cents = int(money.centsValue()[:-1])
            centsHolder = cents
            for i in range(years):
                cents += centsHolder * percentage
            if showmoney:
                return "$" + str(round(cents / 100, decimalplaces))
            else:
                return str(int(cents)) + "¢"


def loanintrest(money: Money, years: int, percentage: List[int or float], showmoney: bool = True, decimalplaces: int = 2, **additionalmoneyeachyear: Money):
    """
    Calculates the loan intrest of the Money borrowed.

    money
    =====
    The money, should be an instance of class Money

    years
    =====
    How long the money has been own to the bank

    percentage
    ==========
    The percentage of money that will have to be payed in extra each year, it can change like this [10, 10, 10, 15](It increased in the third year to fourth year from 5 more cents)

    showmoney
    =========
    A boolean to show if to display in cents or money, default is True

    decimalplaces
    =============
    The decimalplaces to show when rounding off, defualt is 2

    additionalmoneyeacheyear
    ========================
    To prevent confusion, here is an explanation: in there, if there will be extra charges each year, it should be something like this in the parameter: (Money(50), 2, 10, True, 2, year1=Money(50))

    Format: year(number) = Money(whatevervalue). Additionalmoneyeachyear is optional
    """
    if not isinstance(money, Money):
        raise MoneyError(f"money is not an instance of Money, money is an is an instance of {money.__class__.__name__}")
    elif type(years) not in [int or float]:
        raise TypeError(f"Type {type(years)} cannot be for years. Only int or float")
    elif type(percentage) != list:
        raise TypeError(f"Type {type(percentage)} cannot be for percentage. Only List full of ints and floats")
    elif showmoney not in [True, False]:
        if showmoney == None:
            raise SyntaxError("showmoney cannot be None")
        else:
            raise TypeError(f"showmoney cannot be in {type(showmoney)}. Only bool")
    elif type(decimalplaces) != int:
        raise TypeError(f"Type {type(decimalplaces)} cannot be used in decimalplaces. Only integer")
    elif type(additionalmoneyeachyear) != dict:
        raise TypeError(
            f"Type {type(additionalmoneyeachyear)} cannot be used for additionalmoneyeachyear. Only dictionary")
    else:
        if len([p for p in percentage if type(p) in [int, float]]) != len(percentage):
            raise TypeError("Found a non-integer or non-float")
        else:
            try:
                yearnum = [int(k.split("year")[1]) for k in additionalmoneyeachyear.keys()]
                valuetoadd = [int(v.centsValue()[:-1]) for v in additionalmoneyeachyear.values()]
                print(yearnum)
                print(valuetoadd)
                cents = int(money.centsValue()[:-1])
                print(cents)
                centsHolder = cents
                if len(yearnum) < 1:
                    raise Exception("")
                elif len(valuetoadd) < 1:
                    raise Exception("")
                else:
                    for i in range(int(years)):
                        if i in yearnum:
                            cents += centsHolder + valuetoadd[yearnum.index(i)]
                            yearnum = yearnum.remove(i)
                            print(cents)
                        cents += (centsHolder * (percentage[i] / 100))
                        print(cents)
                    print(cents)
                    if showmoney:
                        return "$" + str(round(cents / 100, decimalplaces))
                    else:
                        return Money(cents).centsValue()
            except:
                print("No additionalmoneyeachyear defined")


print(loanintrest(Money(20), 2, [10, 20], True, 5, year1=Money(30), year2=Money(50)))
