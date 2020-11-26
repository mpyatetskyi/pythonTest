#digits = input('Please insert an int:')


class Solution:
    def plusOne(self, digits):

        digits = str(digits)
        intlist = []
        for q in digits:
            intlist.append(int(q))
        digits = intlist

        val = []

        for i in digits:
            val.append(str(i))

        val = int(''.join(val))
        val = val + 1
        val = list(str(val))

        f = []
        for v in val:
            f.append(int(v))

        return f

f = Solution.plusOne(0,99)
print(f)

