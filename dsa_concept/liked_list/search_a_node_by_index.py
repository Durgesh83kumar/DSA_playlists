from common_LL import createLLFromList, print_LL

head = createLLFromList([1,2,3,4,5])
print_LL(head)

def search_by_index(head,index):
    temp = head
    count = 0

    while(temp!=None):
        if(count==index):
            return temp.data
        temp = temp.next
        count += 1

    return None

print("Searching")
print(search_by_index(head,4))