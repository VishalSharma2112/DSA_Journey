class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        maps = {}
        sorted_arr = sorted(set(arr))
        answer = []

        for index, i in enumerate(sorted_arr):
            maps[i] = index+1
        
        for i in arr:
            answer.append(maps[i])
        return answer