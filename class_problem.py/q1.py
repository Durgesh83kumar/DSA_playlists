def binary_search(arr,start,end,target):
   
    
    mid = (start+end)//2
    if(arr[mid]==target):
        return mid
    elif(arr[mid]<target):
        return binary_search(arr,mid+1,end,target)

    elif(arr[mid]>target):
        return binary_search(arr,start,mid-1,target)
    
    else:
        return -1
arr=[3,5,8,9,29]
print(binary_search(arr,0,len(arr)-1,9))