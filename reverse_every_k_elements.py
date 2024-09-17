#Reverse every k elements

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, head, data):
        new_node = Node(data)
        new_node.next = head
        return new_node
    
    def reverse_list(self, head, k):
        if k <=1 or head is None:
            return head
        current, previous = head, None
        while True:
            lastnode_previous_part = previous
            lastnode_sublist = current
            temp = None
            i=0
            while current is not None and i<k:
                temp = current.next
                current.next = previous
                previous =current
                current = temp
                i+=1
            if lastnode_previous_part is not None:
                lastnode_previous_part.next = previous
            else:
                head = previous
            
            lastnode_sublist.next = current
            if current is None:
                break
            previous = lastnode_sublist
        return head
    
    def print_list(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")

object = LinkedList()
head = None
head = object.insert_node(head,8)
head = object.insert_node(head,7)
head = object.insert_node(head,6)
head = object.insert_node(head,5)
head = object.insert_node(head,4)
head = object.insert_node(head,3)
head = object.insert_node(head,2)
head = object.insert_node(head,1)
print("Original List")
object.print_list(head)
print("Reverse every k elements in Linked List")
reversed = object.reverse_list(head, 2)
object.print_list(reversed)


