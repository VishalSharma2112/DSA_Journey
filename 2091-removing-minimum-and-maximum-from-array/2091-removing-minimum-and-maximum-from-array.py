class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = float('-inf')
        max_ind = 0
        min_num = float('inf')
        min_ind = 0
        for index, i in enumerate(nums):
            if i > max_num:
                max_num = i
                max_ind = index
            if i < min_num:
                min_num = i
                min_ind = index
        first = min(max_ind, min_ind)
        second = max(max_ind, min_ind)

        left = second+1
        right = n-first
        both = (first+1) + (n-second)

        return(min(both, left, right))
        