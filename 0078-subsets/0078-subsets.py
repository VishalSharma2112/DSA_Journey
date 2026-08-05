class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for num in range(0, 2**n):
            sub_arr = []
            for i in range(0, n):
                if num & 1<<i:
                    sub_arr.append(nums[i])
            result.append(sub_arr)
        return result