# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy
        while n+1:
            n -= 1
            first = first.next
        while first is not None:
            first=first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
            
        