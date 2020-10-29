#Given two binary strings, return their sum (also a binary string).
#The input strings are both non-empty and contains only characters 1 or 0



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        intsum = int(a,2)+int(b,2)
        binsum = bin(intsum)
        output = binsum[2:]
        return output