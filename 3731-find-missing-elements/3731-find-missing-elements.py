class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        freq_maps = {}
        for i in nums:
            freq_maps[i] = freq_maps.get(i, 0)+1
        low = min(nums)
        high = max(nums)
        for i in range(low, high+1):
            if i not in freq_maps:
                ans.append(i)
        return ans