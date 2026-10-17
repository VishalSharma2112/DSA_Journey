# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return True
        
        stack = []
        fast = head
        slow = head

        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        if fast==None: # even number of nodes
            while slow:
                if stack[-1] == slow.val:
                    slow = slow.next
                    stack.pop()
                else:
                    return False
            return True
        else:
            stack.pop
            slow = slow.next
            while slow:
                if stack[-1] == slow.val:
                    slow = slow.next
                    stack.pop()
                else:
                    return False
            return True