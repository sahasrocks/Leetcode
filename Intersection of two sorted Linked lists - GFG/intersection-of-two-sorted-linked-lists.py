#User function Template for python3

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

def findIntersection(head1,head2):
    #return head
    set1 = set()
    dummy = Node(0)
    temp = dummy
    
    while head1:
        set1.add(head1.data)
        head1 = head1.next
    
    while head2:
        if head2.data in set1 and head2.data != temp.data:
            node = Node(head2.data)
            temp.next = node
            temp = temp.next
        head2 = head2.next
    
    return dummy.next   
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        n1,n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        result = findIntersection(ll1.head,ll2.head)
        printList(result)
        print()

# } Driver Code Ends