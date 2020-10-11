class Factorial:

    def __init__(self):
        '''count factorial to n'''

    def factcount(self, n):
        result = 1
        for param in range(1, n):
            result = result * param
        return result
