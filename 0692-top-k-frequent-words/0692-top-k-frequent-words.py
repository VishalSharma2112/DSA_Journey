class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        maps = {}
        answer = []

        for i in words:
            maps[i] = maps.get(i, 0) + 1
        
        sorted_list = list(sorted(maps.items(), key = lambda x: (-x[1], x[0])))

        for i in range(k):
            answer.append(sorted_list[i][0])

        return answer