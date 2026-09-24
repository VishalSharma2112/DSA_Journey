class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(num):
            Sum = 0
            while num != 0:
                Sum += num % 10
                num //= 10
            return Sum

        for i in range(len(nums)):
            if digit_sum(nums[i]) == i:
                return i

        return -1