# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        move1 = headB
        while move1:
            seen.add(move1)
            move1 = move1.next
        
        move2 = headA
        while move2:
            if move2 in seen:
                return move2
            move2 = move2.next
        return None