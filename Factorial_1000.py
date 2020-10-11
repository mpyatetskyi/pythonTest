from Factorial import Factorial


class FactorialMinus(Factorial):

    def __init__(self):
        Factorial.__init__(self)

    def factmin1000(self, n):
        return super().factcount(n)-10000
