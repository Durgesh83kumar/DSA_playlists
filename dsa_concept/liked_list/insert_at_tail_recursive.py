from common_LL import take_input_better,print_LL

head = take_input_better()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_tail_recursive(head, data):
    if(head is None):
        newNode = Node(data)
        return newNode
    if(head.next == None):
        newNode = Node(data)
        head.next = newNode
        return head
    head.next = insert_at_tail_recursive(head.next,data)
    return head


heat = insert_at_tail_recursive(head,100)
print("After Inserting at Tail")
print_LL(heat)