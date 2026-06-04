from common_LL import *

def reverse_LL_Better(head):
    # Base Case
    # print_LL(head)
    if(head == None or head.next == None): # first always head is None
        return head
    
    smallLinkedListHead = reverse_LL_Better(head.next)
    tailOfReversedList = head.next
    tailOfReversedList.next = head
    head.next = None

    return smallLinkedListHead


head = createLLFromList([1,2,3,4,5])
head = reverse_LL_Better(head)
print_LL(head)