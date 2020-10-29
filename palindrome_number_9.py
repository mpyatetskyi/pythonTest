class Solution:
    def isPalindrome(self, x: int) -> bool:

        reverse = str(x)
        reverse = reverse[::-1]
        x = str(x)

        if reverse == x:
            return True
        elif reverse != x:
            return False