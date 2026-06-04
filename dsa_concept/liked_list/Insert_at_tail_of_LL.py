from common_LL import take_input_better, Node, print_LL

head = take_input_better()
print_LL(head)

def insert_at_tail(head,data): # time complexity is O(n) as while loop runs for n times
    newNode = Node(data)
    if(head is None):
        return newNode
    
    temp = head
    while(temp.next is not None):
        temp = temp.next

    temp.next = newNode

    return head

head = insert_at_tail(head, 100)
print("After Inserting at Tail")
print_LL(head)