class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        max_len = float('inf')
        left = 0
        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                max_len = min(right-left+1, max_len)

                window_sum -= nums[left]
                left += 1
        
        if max_len == float('inf'):
            return 0
        else:
            return max_len