class Solution():

    def __init__(self):
        pass


    def my_func(self,mylist1,mylist2,num):

        if mylist1 == [] or mylist2 == []:
            print('Sorry, you have a blank list')
            return None

        maxsum = None
        for i in mylist1:
            if isinstance(i,str):
                continue
            else:
                for j in mylist2:
                    if isinstance(j,str):
                        continue
                    else:
                        if i+j < num and (maxsum is None or (i+j) > maxsum):
                            maxsum = (i+j)
                        else:
                            continue

        return maxsum



    def my_func_sorted(self,mylist1,mylist2,num):

        if mylist1 == [] or mylist2 == []:
            print('Sorry, you have a blank list')
            return None

        maxsum = None
        mylist1.sort()
        mylist2.sort()
        if mylist1[0] + mylist2[0] > num:
            return None
        for i in mylist1:
            if i + mylist2[0] > num:
                return maxsum
            else:
                for j in mylist2:
                    if i+j < num and maxsum is None:
                        maxsum = (i+j)
                    elif i+j < num:
                        if i+j > maxsum:
                            maxsum = (i+j)
                        else:
                            continue
                    else:
                        break
        return maxsum




a = [1,4,6,2,7,8,9]
b = [-45,-0.9,14,-67,15,-15,228,23,-54]
c = 1000


func = Solution()
print(func.my_func(a,b,c))
print(func.my_func_sorted(a,b,c))
