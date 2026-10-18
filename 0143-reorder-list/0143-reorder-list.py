# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return head
        move = head

        def reverse(head):
            curr = None
            move = head
            while move.next:
                nextNode = move.next
                move.next = curr
                curr = move
                move = nextNode
            move.next = curr
            return move
        
        slow = head
        fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        head2 = reverse(slow.next)
        slow.next = None
        move2 = head2

        dummy = ListNode(0)
        move3 = dummy

        while move and move2:
            move3.next = move
            move = move.next
            move3 = move3.next

            move3.next = move2
            move2 = move2.next
            move3 = move3.next

        if move2==None and move!=None:
            move3.next = move
        return dummy.next