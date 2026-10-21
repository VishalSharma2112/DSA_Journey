# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        def reverse(head):
            move = head
            prev= None
            while move:
                nextNode = move.next
                move.next = prev
                prev = move
                move = nextNode
            return prev
        l1 = reverse(l1)
        l2 = reverse(l2)
        dummy = ListNode(0)
        res = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            Sum = val1 + val2 + carry

            res.next = ListNode(Sum%10)
            carry = Sum//10
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return reverse(dummy.next)