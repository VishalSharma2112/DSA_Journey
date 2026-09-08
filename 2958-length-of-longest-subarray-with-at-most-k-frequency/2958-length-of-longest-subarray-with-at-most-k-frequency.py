class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maps = {}
        left = 0
        ans = 0
        for right in range(len(nums)):
            maps[nums[right]] = maps.get(nums[right], 0)+1

            while maps[nums[right]] > k:
                maps[nums[left]] -= 1
                if maps[nums[left]] == 0:
                    del maps[nums[left]]

                left += 1
            ans = max(ans, right-left+1)
        return ans