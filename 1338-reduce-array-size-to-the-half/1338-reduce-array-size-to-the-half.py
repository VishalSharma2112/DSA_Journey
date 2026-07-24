class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        if len(arr)==2:
            return 1
        n = len(arr)
        maps_freq = {}
        answer = []
        for i in arr:
            maps_freq[i] = maps_freq.get(i, 0)+1
        sorted_maps = sorted(maps_freq.items(), key=lambda x:x[1], reverse=True)
        length = 0
        for i in sorted_maps:
            length += i[1]
            answer.append(i[0])
            if length >= n//2:
                break
        return(len(answer))