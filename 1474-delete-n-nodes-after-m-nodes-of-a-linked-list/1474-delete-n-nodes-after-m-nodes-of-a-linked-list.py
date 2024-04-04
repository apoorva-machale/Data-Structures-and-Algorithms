# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        currentNode = head
        lastMnode = head
        while currentNode:
            mcount = m
            ncount = n
            while currentNode and mcount!=0:
                lastMnode = currentNode
                currentNode = currentNode.next
                mcount -= 1
            while currentNode and ncount!=0:
                currentNode = currentNode.next
                ncount -= 1
            lastMnode.next = currentNode    
        return head
        