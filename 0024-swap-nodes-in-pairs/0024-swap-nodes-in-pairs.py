# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        newhead = head.next
        head.next = newhead.next
        newhead.next = head
        head = newhead
        
        prev = head.next
        move = prev.next
        while move and move.next:
            prev.next = move.next
            move.next = prev.next.next
            prev.next.next = move

            prev = prev.next.next
            move = move.next

        return head