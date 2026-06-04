def rotate_list(lst, k):
    if(len(lst)!=0 and len(lst)!=1):
        for i in range(k):
            l = lst[-1]
            for j in range(len(lst)-1):
                lst[len(lst)-1-j]=lst[len(lst)-2-j]
            lst[0]=l
   
    return lst
a = rotate_list([1,4,2,5],1)
print(a)
