from common_LL import take_input_better, print_LL

head = take_input_better()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_at_tail(head):
    if(head is None or head.next is None):
        return None
    
    temp = head
    while(temp.next.next is not None):
        temp = temp.next

    tail = temp.next
    temp.next = None
    del tail
    return head

head = delete_at_tail(head)
print("After Deletion")
print_LL(head)
