class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        value = {nums[0]: 1}

        for i in range(1, len(nums)):
            if nums[i] in value:
                return True
            else:
                value[nums[i]] = value.get(nums[i], 0) + 1
        
        return False