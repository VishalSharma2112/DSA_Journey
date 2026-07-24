class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        maps_freq = {}
        for i in arr:
            maps_freq[i] = maps_freq.get(i, 0)+1
        for i in arr:
            if maps_freq[i] == 1:
                k-=1
                if k==0:
                    return i
        return ""