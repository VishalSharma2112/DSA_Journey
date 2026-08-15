class Solution(object):
    def removeElement(self, nums, val):
        i= 0 
        j = len(nums) - 1
        while j >= i:
            if nums[j] == val:
                j -= 1
                continue
            elif nums[i] == val:
                nums[i] = nums[j]
                i += 1
                j -= 1
            else:
                i += 1
        return i