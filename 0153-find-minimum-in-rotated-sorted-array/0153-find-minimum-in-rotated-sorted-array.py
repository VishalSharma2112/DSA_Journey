class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums)-1
        mini = float('inf')

        while high>=low:
            mid = low+(high-low)//2

            if nums[low] <= nums[mid]:
                if nums[high] < nums[mid]:
                    low = mid+1
                else:
                    mini = min(mini, nums[mid])
                    high = mid-1
            else:
                if nums[mid] < nums[high]:
                    mini = min(mini, nums[mid])
                    high = mid-1
                else:
                    low = mid+1
        return mini
            
