class Solution():

    def __init__(self):
        pass


    def my_func(self,mylist1,mylist2,mynum):
         mysum = None
         for i in mylist1:
             for j in mylist2:
                 if i+j < mynum and mysum is None:
                     mysum = (i+j)
                 if i+j < mynum and i+j > mysum:
                     mysum = i+j
                 else:
                     continue

         return mysum



    def my_func_sorted(self,mylist1,mylist2,mynum):
        mysum = None
        mylist1.sort()
        mylist2.sort()
        for i in mylist1:
            for j in mylist2:
                if i+j < mynum and mysum is None:
                    mysum = (i+j)
                if i+j < mynum:
                    if i+j > mysum:
                        mysum = (i+j)
                    else:
                        continue
                else:
                    break
        return mysum


    def my_func_reverse_sorted(self,mylist1,mylist2,num):
        mylist1.sort(reverse=True)
        mylist2.sort(reverse=True)
        mysum = None
        for i in mylist1:
            for j in mylist2:
                if i+j > num:
                    continue
                elif i+j < num and mysum is None:
                    mysum = i+j
                    break
                elif i+j < mysum:
                    break
                elif i+j > mysum:
                    mysum = i+j
        return mysum

a = [-1,-4,6,-2]
b = [-45,-1,-14,67]
c = 67


func = Solution()
print(func.my_func(a,b,c))
print(func.my_func_sorted(a,b,c))
print(func.my_func_reverse_sorted(a,b,c))