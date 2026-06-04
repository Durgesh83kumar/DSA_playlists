class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def createLLfromList(lst):
    head = None
    tail = None
    for data in lst:
        newNode = Node(data)
        if(head == None):
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode
        
    return head


def LengthOfLL(head):
    temp = head
    ans = 0
    while(temp != None):
        temp = temp.next
        ans += 1

    return ans

def middleOfLL(head):
    if(head is None or head.next is None):
        return head
    
    length = LengthOfLL(head)
    middle = length//2
    
    temp = head
    count = 0

    while(count<middle):
        temp = temp.next
        count += 1

    return temp

# middle element using 2 pointer
def middleOfLLUsingSlowAndFast(head):
    if(head is None or head.next is None):
        return head
    
    slow = head
    fast = head
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next

    return slow # When fast reaches end, slow will be at middle

headOdd = createLLfromList([10,20,30,40,50])
headEven = createLLfromList([10,20,30,40,50,60])

headOddMid = middleOfLLUsingSlowAndFast(headOdd)
headEvenMid = middleOfLLUsingSlowAndFast(headEven)

print(headOddMid.data)
print(headEvenMid.data)