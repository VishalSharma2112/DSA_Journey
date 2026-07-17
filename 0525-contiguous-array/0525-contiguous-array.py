class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index_maps = {0: -1}
        prefix = 0
        max_length = 0
        for index, i in enumerate(nums):
            length = 0
            if i==0:
                prefix += 1
            else:
                prefix -= 1

            if prefix not in index_maps:
                index_maps[prefix] = index
            else:
                length = index - index_maps[prefix]
            max_length = max(max_length, length)
        return max_length