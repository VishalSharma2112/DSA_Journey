class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while high>=low:
            mid = low + (high-low)//2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            if nums[low]<=nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if target <= nums[high] and target > nums[mid]:
                    low = mid+1
                else:
                    high = mid-1

        return -1