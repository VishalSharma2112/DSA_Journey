# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        move = list1
        count = 1
        while count!=a:
            move = move.next
            count += 1
        
        start = move
        deleteNode = b-a+1
        while count!=deleteNode+a+1:
            move = move.next
            count += 1
        start.next = list2
        while start.next:
            start = start.next
        start.next = move
        return list1