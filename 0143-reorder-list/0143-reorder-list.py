class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return

        def reverse(head):
            curr = None
            move = head

            while move.next:
                nextNode = move.next
                move.next = curr
                curr = move
                move = nextNode

            move.next = curr
            return move

        slow = head
        fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        head2 = reverse(slow.next)
        slow.next = None

        move = head
        move2 = head2

        while move and move2:
            next1 = move.next
            next2 = move2.next

            move.next = move2
            move2.next = next1

            move = next1
            move2 = next2