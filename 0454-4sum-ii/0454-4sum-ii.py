class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        AB_maps = {}
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                AB_maps[nums1[i]+nums2[j]] = AB_maps.get(nums1[i]+nums2[j], 0) + 1
        CD_maps = {}
        for i in range(n):
            for j in range(n):
                CD_maps[nums3[i]+nums4[j]] = CD_maps.get(nums3[i]+nums4[j], 0) + 1
        count = 0
        for num in AB_maps:
            if -num in CD_maps:
                count += AB_maps[num] * CD_maps[-num]

        return count