class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        ans = [0]*len(nums)
        k = len(nums)-1
        while j >= i:
            right = nums[j]**2
            left = nums[i]**2
            if right > left:
                ans[k] = right
                j -= 1
            else:
                ans[k] = left
                i += 1
            k -= 1
        return ans
                