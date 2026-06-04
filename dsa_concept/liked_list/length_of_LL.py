from common_LL import take_input_better, print_LL

def lenghtOfLL(head):
    temp = head
    count = 0
    while(temp is not None):
        count += 1
        temp = temp.next
    
    return count

headOfLL = take_input_better()
length = lenghtOfLL(headOfLL)
print(length)

# lengthOfLLRecursive
def lengthOFLLRecursive(head):
    if(head==None): # Base Case
        return 0
    
    recursiveAnswer = lengthOFLLRecursive(head.next)

    return 1 + recursiveAnswer

length = lengthOFLLRecursive(headOfLL)
print(length)