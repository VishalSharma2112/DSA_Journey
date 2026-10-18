
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1 = l1
        num2 = l2
        carry = 0

        dummy = ListNode(0)
        move = dummy

        while num1 or num2 or carry:
            val1 = num1.val if num1 else 0
            val2 = num2.val if num2 else 0

            Sum = val1 + val2 + carry

            newNode = ListNode(Sum % 10)
            move.next = newNode

            carry = Sum // 10

            if num1:
                num1 = num1.next

            if num2:
                num2 = num2.next

            move = move.next

        return dummy.next
