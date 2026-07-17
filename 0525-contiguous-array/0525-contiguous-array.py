class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index_maps = {0: -1}
        prefix = 0
        max_length = 0
        for index, i in enumerate(nums):
            if i==0:
                prefix -= 1
            else:
                prefix += 1

            if prefix not in index_maps:
                index_maps[prefix] = index
            else:
                max_length = max(index - index_maps[prefix], max_length)
        return max_length