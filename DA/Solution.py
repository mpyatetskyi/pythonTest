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




