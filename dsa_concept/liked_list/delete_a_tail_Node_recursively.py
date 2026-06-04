from common_LL import take_input_better, print_LL

head = take_input_better()

def delete_tail_recursive(head):
    if(head is None):
        return None
    
    if(head.next is None):
        del head
        return None
    
    head.next = delete_tail_recursive(head.next)
    return head

head = delete_tail_recursive(head)
print("After Deletion")
print_LL(head)