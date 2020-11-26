# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        a = []
        num = list(bin(num)[2:])
        for nums in num:
            if nums == '1':
                a.append('0')
            if nums == '0':
                a.append('1')

        a = int(''.join(a), 2)
        return a