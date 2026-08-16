class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        k = 0
        while i < len(nums):
            if nums[i] != nums[i-1]:
                k += 1
                nums[k] = nums[i]
            i += 1
        return k+1