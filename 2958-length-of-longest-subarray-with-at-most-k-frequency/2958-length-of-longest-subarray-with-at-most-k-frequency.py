class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maps = {}
        left = 0
        ans = 0
        for i in range(len(nums)):
            maps[nums[i]] = maps.get(nums[i], 0)+1
            while maps[nums[i]] > k:
                maps[nums[left]] -= 1
                left += 1
            ans = max(ans, i-left+1)
        return ans