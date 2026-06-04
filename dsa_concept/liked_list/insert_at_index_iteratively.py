from common_LL import take_input_better, print_LL

head = take_input_better()
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert_at_index(head,data,index):
    if(index==0):
        newNode = Node(data)
        newNode.next = head
        head = newNode
        return head
    newNode = Node(data)
    temp = head
    count = 0

    while(temp is not None and count < index - 1):
        temp = temp.next
        count += 1

    if(temp is None):
        print("Index out of bounds, please check index")
        return head

    newNode.next = temp.next
    temp.next = newNode
    return head

head = insert_at_index(head,35,3)
print("After Inserting at Index")
print_LL(head)