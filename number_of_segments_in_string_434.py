# https://leetcode.com/problems/number-of-segments-in-a-string/
class Solution:
    def countSegments(self, s: str) -> int:
        s = len(s.split())
        return s