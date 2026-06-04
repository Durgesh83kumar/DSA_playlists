from common_LL import *

def reverse_LL(head):
    print_LL(head)
    # Base Case
    if(head == None or head.next == None): # first always head is None
        return head
    
    smallLinkedListHead = reverse_LL(head.next)

    temp = smallLinkedListHead
    while(temp.next is not None):
        temp = temp.next

    temp.next = head
    head.next = None

    return smallLinkedListHead

head = createLLFromList([1,2,3,4,5])
head = reverse_LL(head)
print_LL(head)