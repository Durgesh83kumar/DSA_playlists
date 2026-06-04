from common_LL import take_input_better, print_LL

head = take_input_better()
print_LL(head)

def delete_at_index_recursively(head, index):
    if(head is None):
        print("Index is Out of Bound")
        return None
    
    if(index == 0):
        temp = head
        head = temp.next
        del temp
        return head
    
    head.next = delete_at_index_recursively(head.next,index-1)

    return head

head = delete_at_index_recursively(head,3)
print("After deletion")
print_LL(head)