class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower(nums, target):
            mini = -1
            low = 0
            high = len(nums)-1

            while high>=low:
                mid = (low+high)//2
                if nums[mid] >= target:
                    high = mid-1
                    mini = mid
                else:
                    low = mid+1
            return mini

        def higher(nums, target):
            maxi = -1
            low = 0
            high = len(nums)-1

            while high>=low:
                mid = (low+high)//2

                if nums[mid] <= target:
                    low = mid+1
                    maxi = mid
                else:
                    high = mid-1
            return maxi
        lowerNum = lower(nums, target)
        higherNum = higher(nums, target)
        if lowerNum == -1 or nums[lowerNum] != target:
            return [-1, -1]

        return [lowerNum, higherNum]