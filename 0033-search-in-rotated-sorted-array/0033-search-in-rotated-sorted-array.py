class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for index, i in enumerate(nums):
            if i == target:
                return index
        return -1