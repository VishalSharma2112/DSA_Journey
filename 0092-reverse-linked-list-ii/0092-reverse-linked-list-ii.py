
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if head is None or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        leftList = dummy
        for i in range(left - 1):
            leftList = leftList.next

        prev = None
        curr = leftList.next

        for i in range(right - left + 1):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        leftList.next.next = curr
        leftList.next = prev

        return dummy.next
