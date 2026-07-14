class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)/2
        maps = {}

        for i in nums:
            maps[i] = maps.get(i, 0) + 1
            if maps[i] > length:
                return i