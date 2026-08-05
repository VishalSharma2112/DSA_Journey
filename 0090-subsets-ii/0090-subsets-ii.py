class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = set()
        for num in range(0, 2**n):
            sub_arr = []
            for i in range(0, n):
                if num & 1<<i:
                    sub_arr.append(nums[i])
            result.add(tuple(sub_arr))
                    
        return [list(x) for x in result]