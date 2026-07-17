class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        n = len(nums)
        left_sum = 0

        for i in range(n):
            if(left_sum == total-left_sum-nums[i]):
                return i
            else:
                left_sum = left_sum + nums[i]
        return -1
