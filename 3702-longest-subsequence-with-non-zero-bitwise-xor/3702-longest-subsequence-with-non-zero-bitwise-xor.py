class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        xor = 0
        has_non_zero = False

        for x in nums:
            xor ^= x
            if x != 0:
                has_non_zero = True

        if xor != 0:
            return len(nums)

        if not has_non_zero:
            return 0

        return len(nums) - 1