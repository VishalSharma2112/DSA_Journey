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
        curr = head
        prev = dummy

        while curr and curr.next:
            if curr.next.val == curr.val:
                while curr.next and curr.next.val == curr.val:
                    curr = curr.next  
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
            
        return dummy.next
