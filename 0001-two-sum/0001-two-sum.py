class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value = {nums[0]: 0}
        n = len(nums)
        for i in range(1, n):
            if target - nums[i] in value :
                return [value[target-nums[i]], i]
            else:
                value[nums[i]] = i