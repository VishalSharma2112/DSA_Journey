# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        count = 1
        dummy1 = ListNode(0)
        move1 = dummy1

        dummy2 = ListNode(0)
        move2 = dummy2

        move = head
        while move:
            if count%2 == 1:   # odd
                move1.next = move
                move1 = move1.next
            else:   # even
                move2.next = move
                move2 = move2.next
            count += 1
            move = move.next

        move2.next = None
        move1.next = dummy2.next
        return dummy1.next