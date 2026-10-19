class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans = []
        nums.sort()
        for index, i in enumerate(nums):
            if i == target:
                ans.append(index)
        return ans