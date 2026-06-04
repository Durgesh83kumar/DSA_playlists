from common_LL import take_input_better, print_LL

head = take_input_better()
print_LL(head)

def delete_node_at_given_index(head,index):
    if(head is None):
        return None
    
    if(index == 0):
        temp = head
        head = head.next
        del temp
        return head
    
    
    temp = head
    count = 0
    while(temp is not None and count<index-1):
        temp = temp.next
        count += 1

    if(temp is None or temp.next is None):
        print("Out of Bounds")
        return head
    

    deleted_node = temp.next
    nodeAfter_deleted_node = deleted_node.next 
    temp.next = nodeAfter_deleted_node   #temp.next.next
    del deleted_node
    return head


head = delete_node_at_given_index(head,3)
print("After Deletion")
print_LL(head)