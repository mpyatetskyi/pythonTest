class Solution:
    def reverse(self, x: int) -> int:

        const = range((-2) ** 31, (2) ** 31 - 1)
        if not x in const:
            x = 0
        elif x < 0:
            x = x * (-1)
            x = str(x)
            x = x[::-1]
            x = int(x) * (-1)
            if not x in const:
                x = 0
        elif x > 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if not x in const:
                x = 0
        elif x == 0:
            x = 0

        return x