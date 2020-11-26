class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 0:
            return 0
        if needle in haystack:
            ind = haystack.index(needle, 0)
            return ind
        if not needle in haystack:
            return -1