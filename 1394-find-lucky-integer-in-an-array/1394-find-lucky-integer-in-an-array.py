class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_maps = {}
        max_len = -1
        for i in arr:
            freq_maps[i] = freq_maps.get(i, 0)+1
        for i in freq_maps:
            if freq_maps[i] == i:
                max_len = max(max_len, freq_maps[i])
        return max_len