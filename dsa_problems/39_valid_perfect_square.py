# def is_perfect_square(num):
    # n = int(num**0.5)
    # if(n*n == num):
        # return True
    # else:
        # return False
# 
# print(is_perfect_square(9))


#_______________________ by binary Search_________________________

def is_perfect_square(num):
    start = 0
    end = num
    while(start<=end):
        mid = (start+end)//2
        if(mid*mid==num):
            return True
        elif(mid*mid<num):
            start = mid+1
        else:
            end = mid-1
    
    return False

print(is_perfect_square(81))