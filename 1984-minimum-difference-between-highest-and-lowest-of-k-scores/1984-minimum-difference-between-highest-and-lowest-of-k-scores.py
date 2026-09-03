class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        min_diff = float('inf')
        for right in range(len(nums)):
            if right-left+1 == k:
                min_diff = min(min_diff, nums[right]-nums[left])
                left += 1
        return min_diff