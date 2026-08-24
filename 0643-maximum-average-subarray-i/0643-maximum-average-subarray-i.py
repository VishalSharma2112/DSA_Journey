class Solution(object):
    def findMaxAverage(self, nums, k)->float:
        left = 0
        Sum = 0
        max_sum = float("-inf")
        for right in range(len(nums)):
            Sum += nums[right]
            
            if right-left+1 == k:
                max_sum = max(Sum, max_sum)
                Sum -= nums[left]
                left += 1
        return max_sum/k
        