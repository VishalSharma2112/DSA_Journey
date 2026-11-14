class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binarySearch(start, end):
            if start>end:
                return -1

            mid = start + (end-start)//2

            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                return binarySearch(start, mid-1)
            else:
                return binarySearch(mid+1, end)

        return binarySearch(0, len(nums)-1)
            