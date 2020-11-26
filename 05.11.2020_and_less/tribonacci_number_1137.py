# https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci(self, n: int) -> int:
        nrange = range(0, 38)
        if n in nrange:

            c = 0
            fibsum = 0
            fiblist = [0, 0, 1]
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            if n >= 3:
                while c <= n + 3:
                    a = fiblist[-1] + fiblist[-2] + fiblist[-3]
                    fiblist.append(a)
                    c += 1
                fibsum = fiblist[n + 1]
            return fibsum
