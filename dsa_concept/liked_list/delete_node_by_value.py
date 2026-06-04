from common_LL import take_input_better, print_LL

head = take_input_better()
print_LL(head)

def delete_node_by_value(head,value):
    if(head is None):
        print("List is empty")
        return None
    
    if(head.data == value):
        temp = head
        head = temp.next
        del temp
        return head.next # Boundary case when head is value
    
    temp = head

    while(temp.next is not None and temp.next.data != value):
        temp = temp.next

    if(temp.next is None):
        print("value is not present")
        return head

    nodeToBeDeleted = temp.next
    nodeAfterDeletedNode = nodeToBeDeleted.next
    temp.next = nodeAfterDeletedNode
    del nodeToBeDeleted

    return head

head = delete_node_by_value(head, 20)
print("After deletion")
print_LL(head)    
