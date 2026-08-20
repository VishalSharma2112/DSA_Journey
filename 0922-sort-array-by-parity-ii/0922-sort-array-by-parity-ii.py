class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = 1
        while j<n and i < n:
            if nums[i] % 2 != 0:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                i += 2
            
            if nums[j] % 2 == 0:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                j += 2
        return(nums)