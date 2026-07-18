class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        maps_freq = {}
        for i in nums1:
            maps_freq[i] = maps_freq.get(i, 0) + 1
        for i in nums2:
            if i in maps_freq and maps_freq[i] != 0:
                answer.append(i)
                maps_freq[i] -= 1
        return answer