class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while end>=start:
            mid = start + (end-start)//2
            print(start, end)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid+1
            else:
                end = mid-1
        return start
        