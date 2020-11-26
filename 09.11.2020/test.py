from typing import List

arr = [3,1,7,11,3.5]
arrr = ['s']

class Solution:
    def checkIfExist(self, arr : List[int]) -> bool:
        print(arr)
        for a in arr:

            if a * 2 in arr or a / 2 in arr:
                return True

        return False


a = Solution.checkIfExist(1, arrr)
print(a)