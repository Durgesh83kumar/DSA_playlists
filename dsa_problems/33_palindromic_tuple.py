def is_palindromic_tuple(tup):
    # Your code goes here
    start = 0
    end = len(tup)-1
    while(start<end):
        if(tup[start]!=tup[end]):
            return False
        start += 1
        end -= 1
        
    return True

tup = (1,2,3,2,1)
print(is_palindromic_tuple(tup))