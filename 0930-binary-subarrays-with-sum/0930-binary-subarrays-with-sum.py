class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq_sum = {0: 1}
        count = 0
        prefix = 0

        for num in nums:
            prefix += num
            if prefix-goal in freq_sum:
                count += freq_sum[prefix-goal]
            freq_sum[prefix] = freq_sum.get(prefix, 0) + 1
        return count