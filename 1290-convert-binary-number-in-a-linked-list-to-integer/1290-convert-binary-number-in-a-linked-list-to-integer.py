# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current = head
        number = []
        index = 0
        result=0
        while current:
            number.append(current.val)
            current = current.next
            
        for i in range(len(number)):
            if number[i]:
                result += 2 ** (len(number)-i-1)
        return result
            