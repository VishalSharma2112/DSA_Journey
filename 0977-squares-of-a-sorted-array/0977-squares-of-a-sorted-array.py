class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        ans = []
        while j >= i:
            right = nums[j]**2
            left = nums[i]**2
            if right > left:
                ans.append(right)
                j -= 1
            else:
                ans.append(left)
                i += 1
        return ans[::-1]