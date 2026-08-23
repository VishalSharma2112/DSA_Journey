class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = len(nums)//2
        ans = []
        while j < len(nums):
            ans.append(nums[i])
            ans.append(nums[j])
            i += 1
            j += 1
        return ans