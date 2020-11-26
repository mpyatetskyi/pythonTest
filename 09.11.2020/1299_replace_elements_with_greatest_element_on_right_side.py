# 1299. Replace Elements with Greatest Element on Right Side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mymax = 0
        mylist = []
        for i in range(1, len(arr)):
            if len(arr[i:]) == 1:
                mymax = arr[-1]
                mylist.append(mymax)
            else:
                mymax = max(arr[i:])
                mylist.append(mymax)
        mylist.append(-1)
        return mylist