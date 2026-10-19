# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        if not head.next.next:
            return head.val + head.next.val
        
        def reverse(head):
            prev = None
            curr = head
            while curr:
                newNode = curr.next
                curr.next = prev
                prev = curr
                curr = newNode
            return prev
        
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = reverse(slow.next)
        slow.next = None

        max_sum = -1
        move1 = head
        move2 = head2
        while move1:
            max_sum = max(move1.val + move2.val, max_sum)
            move1 = move1.next
            move2 = move2.next

        return max_sum