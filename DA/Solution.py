class Solution():

    def __init__(self):
        pass


    def my_func(self,mylist1,mylist2,mynum):
         mysum: int = 0
         for i in mylist1:
             for j in mylist2:
                 if i+j < mynum:
                     mysum += (i+j)
                 else:
                     continue

         return mysum



    def my_func2(self,mylist1,mylist2,mynum):
        mysum = 0
        mylist1.sort()
        mylist2.sort()
        for i in mylist1:
            for j in mylist2:
                if i+j < mynum:
                    mysum += (i+j)
                else:
                    break
        return mysum


    def my_func3(self,mylist1,mylist2,num):
        mylist1.sort(reverse = True)
        mylist2.sort(reverse = True)

        if mylist1[0] + mylist2[0] < num:
            return mylist1[0] + mylist2[0]


a = [1,4,6,]
b = [45,1,14,67]
c = 100


func = Solution()
print(func.my_func3(a,b,c))