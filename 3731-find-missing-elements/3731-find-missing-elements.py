class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set(nums)
        low, high = min(nums), max(nums)
        for i in range(low, high+1):
            if i not in seen:
                ans.append(i)
        return ans