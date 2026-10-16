# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        move = dummy
        while list1 and list2:
            if list1.val > list2.val:
                move.next = list2
                list2 = list2.next
            else:
                move.next = list1
                list1 = list1.next
            move = move.next
        
        if list1==None and list2!=None:
            move.next = list2
        if list2==None and list1!=None:
            move.next = list1
        return dummy.next