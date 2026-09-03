class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        max_grumpy = 0
        left = 0
        window_grumpy = 0

        for right in range(len(grumpy)):
            if grumpy[right] == 0:
                satisfied += customers[right]
            else:
                window_grumpy += customers[right]
            
            if right-left+1 == minutes:
                max_grumpy = max(max_grumpy, window_grumpy)

                if grumpy[left] == 1:
                    window_grumpy -= customers[left]
                left += 1
        return satisfied + max_grumpy