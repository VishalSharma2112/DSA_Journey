# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head:
            return None
        if not head.next and n==1:
            return None
        
        fast = head
        slow = head

        for i in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            
        if fast==None:
            return head.next

        slow.next = slow.next.next
        return head
        
        