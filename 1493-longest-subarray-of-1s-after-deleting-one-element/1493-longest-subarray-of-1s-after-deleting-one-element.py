class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        window_cnt = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] != 1:
                window_cnt += 1
            
            while window_cnt > 1:
                max_len = max(right-left, max_len)

                if nums[left] != 1:
                    window_cnt -= 1
                left += 1

        return max(right-left, max_len-1)