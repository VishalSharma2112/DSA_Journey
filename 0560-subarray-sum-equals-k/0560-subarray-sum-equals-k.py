class Solution:
    def subarraySum(self, nums, k):
        prefix = 0
        maps = {0:1}
        answer = 0

        for i in nums:
            prefix = i+prefix
            if prefix-k in maps:
                answer = answer + maps[prefix-k]
            maps[prefix] = maps.get(prefix, 0) + 1
        return answer
