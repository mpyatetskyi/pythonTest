# https://leetcode.com/problems/fizz-buzz/submissions/

class Solution:
    def fizzBuzz(self, n):
        a = []
        for val in range(1,n+1):
            if val%3 == 0 and val%5 == 0:
                a.append('FizzBuzz')
            elif val%3 == 0:
                a.append('Fizz')
            elif val%5 == 0:
                a.append('Buzz')
            else:
                a.append(str(val))
        return a


