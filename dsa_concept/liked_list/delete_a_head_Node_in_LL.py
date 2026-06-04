from common_LL import Node, take_input_better, print_LL
head = take_input_better()
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_at_head(head):
    if(head is None):
        return None
    newNode = head
    head = head.next
    del newNode
    return head

print_LL(head)
head = delete_at_head(head)
print("After Deletion")
print_LL(head)