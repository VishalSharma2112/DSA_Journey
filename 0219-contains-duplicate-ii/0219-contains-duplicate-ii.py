class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value = {nums[0]: 0}

        for i in range(1, len(nums)):
            if (nums[i] in value and (i - value[nums[i]] <= k)):
                return True
            else:
                value[nums[i]] = i
        
        return False