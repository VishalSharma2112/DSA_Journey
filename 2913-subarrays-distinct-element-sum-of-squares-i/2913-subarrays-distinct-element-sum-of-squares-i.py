class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for k in range(1, len(nums)+1):
            left = 0
            freq = {}
            for right in range(len(nums)):
                freq[nums[right]] = freq.get(nums[right], 0)+1
                if right-left+1 == k:
                    ans = ans + (len(freq)**2)
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
        return ans