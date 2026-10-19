# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        
        prev = head
        move = head.next
        while move:
            if prev.val == move.val:
                prev.next = move.next
            else:
                prev = move
            move = move.next

        return dummy.next
