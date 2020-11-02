# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        fiblist = []
        answer = 0
        while len(fiblist) <= N:
            fiblist.append(a)
            a, b = b, a + b
        if N in range(0, 31):
            if N == 0:
                answer = 0
            if N == 1:
                answer = 1
            if N >= 2:
                answer = fiblist[N - 1] + fiblist[N - 2]
        return answer

