"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        move = head
        while move:
            newNode = Node(move.val, move.next)
            move.next = newNode
            move = move.next.next

        move = head
        while move:
            if move.random!=None:
                move.next.random = move.random.next
            move = move.next.next

        dummy = Node(0)
        res = dummy
        move = head
        while move:
            res.next = move.next
            move.next = move.next.next
            res = res.next
            move = move.next
        return dummy.next