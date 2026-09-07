class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        freq = set()
        min_len = float('inf')
        left = 0

        for right in range(len(cards)):
            while cards[right] in freq:
                min_len = min(min_len, right-left+1)
                freq.remove(cards[left])
                left += 1


            freq.add(cards[right])
        return -1 if min_len == float('inf') else min_len