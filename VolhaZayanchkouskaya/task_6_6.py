"""
Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition
and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores information
about exchange rates to your default currency:

exchange_rate = {
    "EUR": 0.93,
    "BYN": 2.1,
    ...
}
Example:

x = Money(10, "BYN")
y = Money(11) # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8) # result in “EUR”
>>543.21 EUR

lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s) #result in “BYN”
>>123.45 BYN
Have a look at @functools.total_ordering
"""


import functools


@functools.total_ordering
class Money:
    exchange_rate = {
        "EUR": 2.92,
        "BYN": 1.0,
        "USD": 2.50,
        "RUB": 0.0344,
    }

    def __init__(self, value: (int, float), currency: str = "BYN"):
        self._value = value
        self._currency = currency
        self._exvalue = self._value * self.exchange_rate[self._currency]

    def __eq__(self, other):
        return self._exvalue == other._exvalue

    def __lt__(self, other):
        return self._exvalue < other._exvalue

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self._value + other._exvalue / self.exchange_rate[self._currency], self._currency)
        elif isinstance(other, (int, float)):
            return Money(self._value + other, self._currency)
        else:
            raise NotImplemented

    def __radd__(self, other):
        return Money(other + self._value, self._currency)

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(self._value - other._exvalue / self.exchange_rate[self._currency], self._currency)
        elif isinstance(other, (int, float)):
            return Money(self._value - other, self._currency)
        else:
            return NotImplemented

    def __rsub__(self, other):
        return Money(other - self._value, self._currency)

    def __mul__(self, other):
        if isinstance(other, Money):
            return Money(self._value * other._exvalue / self.exchange_rate[self._currency], self._currency)
        elif isinstance(other, (int, float)):
            return Money(self._value * other, self._currency)
        else:
            raise NotImplemented

    def __rmul__(self, other):
        return Money(other * self._value, self._currency)

    def __truediv__(self, other):
        if isinstance(other, Money):
            return Money(self._value / (other._exvalue * self.exchange_rate[self._currency]), self._currency)
        elif isinstance(other, (int, float)):
            if other != 0:
                return Money(self._value / other, self._currency)
            else:
                raise ZeroDivisionError
        else:
            raise NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            if self._value != 0:
                return Money(other / self._value, self._currency)
            else:
                raise ZeroDivisionError
        else:
            raise NotImplemented

    def __str__(self):
        return f"{self._value:.2f} {self._currency}"


if __name__ == "__main__":
    x = Money(10, "RUB")
    y = Money(11)
    z = Money(12.34, "EUR")

    print(z + 0.8 * y + x * 3.11)
    print(x <= z)

    lst = [Money(10, "RUB"), Money(11), Money(12.01, "EUR")]
    s = sum(lst)
    print(s)

