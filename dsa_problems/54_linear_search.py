def linear_search(arr,target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return i
        
    return -1

arr = [10,20,39,50,37]
result = linear_search(arr,10)
print(result)