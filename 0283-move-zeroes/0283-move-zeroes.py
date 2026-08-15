class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 0
        while j<len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j+=1
