class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini = float('inf')
        for size in range(l, r+1):
            left = 0
            window_sum = 0
            for right in range(len(nums)):
                window_sum += nums[right]
                if right-left+1 == size:
                    if window_sum < mini and window_sum>0:
                        mini = window_sum
                    window_sum -= nums[left]
                    left += 1
        return -1 if mini==float('inf') else mini
