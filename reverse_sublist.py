#reverse a sublist p=3, q=5
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node(self, head, data):
        """Inserts a new node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = head
        return new_node

    def reverse_sublist(self, head, p, q):
        if p == q:
            return head
        current = head
        previous = None
        i =0
        while current is not None and i<p-1:
            previous = current
            current = current.next
            i+=1
        
        last_firstpart = previous
        first_lastpart = current
        next_temp = None

        i=0
        while current is not None and i < q-p+1:
            next_temp = current.next
            current.next = previous
            previous = current
            current = next_temp
            i+=1

        if last_firstpart is not None:
            last_firstpart.next = previous
        else:
            head = previous

        if current is not None: 
            first_lastpart.next = current
        else:
            first_lastpart.next = None
        return head
        
    def print_list(self, head):
        """Prints the nodes of the linked list."""
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")

object = LinkedList()
head = None
head = object.insert_node(head, 5)
head = object.insert_node(head, 4)
head = object.insert_node(head, 3)
head = object.insert_node(head, 2)
head = object.insert_node(head, 1) 

print("Original list:")
object.print_list(head) 
reversed_head = object.reverse_sublist(head,2,5)
print("Reversed entire list:")
LinkedList().print_list(reversed_head)