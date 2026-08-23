class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        MAX = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                MAX = max(count, MAX)
            else:
                count = 0
        return MAX
        