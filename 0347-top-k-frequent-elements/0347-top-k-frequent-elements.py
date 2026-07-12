class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        answer = []
        for i in nums:
            maps[i] = maps.get(i, 0) + 1

        sorted_list = sorted(maps.items(), key=lambda x:x[1], reverse = True)

        for i in range(k):
            answer.append(sorted_list[i][0])

        return answer