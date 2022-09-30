from collections import namedtuple

from util import gcd


class Rational(namedtuple('Rational', ['num', 'denom'])):
    def __new__(cls, x, y):
        if y == 0:
            raise ValueError('Denominator cannot be null')
        if y < 0:
            x, y = -x, -y

        return super().__new__(cls, x // gcd(x, y), y // gcd(x, y))

    def __str__(self):
        return '{}/{}'.format(self.num, self.denom)


