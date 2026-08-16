class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        print(xor)
        if xor != 0:
            return len(nums)
        for i in nums:
            if i != 0:
                return len(nums)-1
        return 0