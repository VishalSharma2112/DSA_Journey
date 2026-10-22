"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        stack = []
        move = head
        while move:
            if move.child != None:
                if move.next:
                    move.next.prev = None
                    stack.append(move.next)
                move.next = move.child
                move.child.prev = move
                move.child = None
            move = move.next
        move = head
        
        while stack:
            while move.next:
                move = move.next
            
            move.next = stack[-1]
            stack[-1].prev = move

            stack.pop()
        return head