
class Solution:
    def reverseEvenLengthGroups(self, head):
        prev = head
        group_size = 2

        while prev and prev.next:
            # Count the actual nodes in this group
            curr = prev.next
            count = 0

            while curr and count < group_size:
                curr = curr.next
                count += 1

            # Reverse the group if its length is even
            if count % 2 == 0:
                group_prev = curr
                node = prev.next

                for _ in range(count):
                    nxt = node.next
                    node.next = group_prev
                    group_prev = node
                    node = nxt

                # Connect the reversed group to the list
                tail = prev.next
                prev.next = group_prev
                prev = tail

            else:
                # Skip the group without reversing
                for _ in range(count):
                    prev = prev.next

            group_size += 1

        return head
