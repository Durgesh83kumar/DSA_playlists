from common_LL import Node, take_input_better, print_LL

head = take_input_better()
print_LL(head)

def insert_at_head(head, data): # O(1)
    newNode = Node(data)
    newNode.next = head
    head = newNode
    return head   # we are returning head because here head is getting changed

head = insert_at_head(head, 100)
print("After Inserting at head")
print_LL(head)


