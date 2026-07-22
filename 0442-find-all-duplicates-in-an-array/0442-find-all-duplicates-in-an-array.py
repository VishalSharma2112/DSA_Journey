class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return []
        
        maps_freq = {}
        answer = []
        for i in nums:
            maps_freq[i] = maps_freq.get(i, 0)+1
            if maps_freq[i]>1:
                answer.append(i)
        return answer