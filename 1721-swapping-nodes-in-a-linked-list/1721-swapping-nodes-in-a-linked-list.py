# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        move = dummy
        for i in range(k):
            move = move.next
        initial = move

        slow = head
        while move.next:
            slow = slow.next
            move = move.next
        
        temp = slow.val
        slow.val = initial.val
        initial.val = temp
        
        return head