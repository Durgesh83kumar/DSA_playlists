from common_LL import *

def reverse_LL_Iteratively(head):
    if(head is None or head.next is None):
        return head
    
    prev = None
    current = head

    while(current is not None):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

head = reverse_LL_Iteratively(createLLFromList([1,2,3,4,5]))
print_LL(head)