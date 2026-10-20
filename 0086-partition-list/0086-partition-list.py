# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        if not head or not head.next:
            return head

        dummy1 = ListNode(0)
        move1 = dummy1

        dummy2 = ListNode(0)
        move2 = dummy2

        move = head
        while move:
            if move.val < x:
                move1.next = move
                move1 = move1.next
            else:
                move2.next = move
                move2 = move2.next
            move = move.next
        move2.next = None
        move1.next = dummy2.next
        return dummy1.next

