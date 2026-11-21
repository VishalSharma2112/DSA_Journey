class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        for index, i in enumerate(nums):
            if i == target:
                return True
        return False
        