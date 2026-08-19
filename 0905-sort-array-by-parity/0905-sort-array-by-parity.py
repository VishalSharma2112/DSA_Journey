class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1

        while j > i:
            if nums[i]%2 != 0:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
            
            if nums[j]%2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                j -= 1
        return nums