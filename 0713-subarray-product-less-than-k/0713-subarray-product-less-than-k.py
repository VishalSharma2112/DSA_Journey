class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        count = 0
        window_prod = 1

        for right in range(len(nums)):
            window_prod *= nums[right]
            while window_prod >= k:
                window_prod //= nums[left]
                left += 1
            count += (right-left+1)

        return(count)
        