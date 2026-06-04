from common_LL import take_input_better,print_LL

head = take_input_better()
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert_at_index_recursive(head,data,index):
    if(index==0):
        newNode = Node(data)
        newNode.next = head
        head = newNode
        return head
    if(head == None):
        print("Index is out of bounds")
        return head
    
    head.next = insert_at_index_recursive(head.next,data,index-1)
    return head

head = insert_at_index_recursive(head,35,3)
print("After Inserting at Index")
print_LL(head)