# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        move = head
        for i in range(k-1):
            move = move.next
        initial = move

        slow = head
        while move.next:
            slow = slow.next
            move = move.next
        
        slow.val, initial.val = initial.val, slow.val
        
        return head