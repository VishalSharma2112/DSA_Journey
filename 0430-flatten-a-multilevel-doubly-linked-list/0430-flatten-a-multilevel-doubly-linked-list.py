class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        stack = []
        move = head

        while move:
            if move.child:
                if move.next:
                    stack.append(move.next)

                move.next = move.child
                move.next.prev = move
                move.child = None

            elif not move.next and stack:
                move.next = stack.pop()
                move.next.prev = move

            move = move.next

        return head