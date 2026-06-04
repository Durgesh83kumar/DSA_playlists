def is_palindrome(lst):
    n = len(lst)
    start = 0
    end = n-1
    while(start<end):
        if(lst[start]!=lst[end]):
            return False
        
        start += 1
        end -= 1

    return True
print(is_palindrome([1,2,2,1]))