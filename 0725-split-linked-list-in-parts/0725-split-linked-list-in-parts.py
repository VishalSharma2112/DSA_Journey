# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        move = head
        count = 0
        while move:
            count += 1
            move = move.next

        curr = head
        base_len = count // k
        extra = count % k
        res = []
        for i in range(k):
            res.append(curr)

            for j in range(base_len - 1 + (1 if extra else 0)):
                if not curr: break
                curr = curr.next
            extra -= (1 if extra else 0)
            if curr:
                curr.next, curr = None, curr.next
        return res