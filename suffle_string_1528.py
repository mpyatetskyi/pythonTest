# https://leetcode.com/problems/shuffle-string/submissions/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)
        mylist = []
        for a, b in zip(s, indices):
            mylist.append((b, a))
        mylist.sort()
        mylist = [b for a, b in mylist]
        mylist = ''.join(mylist)
        return mylist
