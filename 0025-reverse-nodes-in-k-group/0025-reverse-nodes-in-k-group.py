# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        move = head
        while move:
            move = curr
            for _ in range(k-1):
                if not move:
                    return dummy.next
                move = move.next
        
            if not move:
                return dummy.next

            nextNode = move.next
            move.next = None

            prev.next = reverse(curr)
            curr.next = nextNode

            prev = curr
            curr = nextNode
        return dummy.next