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

        try:
            my_sorted_list_1 = sorted(mylist1)
        except:
            my_sorted_list_1 = []
            for value in mylist1:
                if isinstance(value,str):
                    continue
                else:
                    my_sorted_list_1.append(value)
            my_sorted_list_1.sort()

        try:
            my_sorted_list_2 = sorted(mylist2)
        except:
            my_sorted_list_2 = []
            for value in mylist2:
                if isinstance(value,str):
                    continue
                else:
                    my_sorted_list_2.append(value)
            my_sorted_list_2.sort()

        maxsum = None

        if my_sorted_list_1[0] + my_sorted_list_2[0] > num:
            return None
        for i in my_sorted_list_1:
            if i + my_sorted_list_2[0] > num:
                return maxsum
            else:
                for j in my_sorted_list_2:
                    if i+j > num:
                        break
                    elif i+j < num and (maxsum is None or i+j > maxsum):
                        maxsum = (i+j)
                    else:
                        continue

        return maxsum




a = [1,-4,'s',6,2,-7,8,9,-99]
b = [-45,'a',0.9,-14,67,-15,'b',15,-228,23,54]
c = 1000


func = Solution()
print(func.my_func(a,b,c))
print(func.my_func_sorted(a,b,c))
