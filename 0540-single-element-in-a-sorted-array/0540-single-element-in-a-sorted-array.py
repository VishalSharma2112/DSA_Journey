class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        n = len(nums)
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]

        low = 1
        high = n-2
        while high>=low:
            mid = (high+low)//2

            if nums[mid-1]!=nums[mid] and nums[mid]!=nums[mid+1]:
                return nums[mid]

            if mid%2 == 0 and nums[mid] == nums[mid-1] or mid%2 == 1 and nums[mid] != nums[mid-1]:
                high = mid-1
            else:
                low = mid+1

