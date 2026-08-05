class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        prefix = [0]
        for i in arr:
            prefix.append(prefix[-1]^i)
        for left, right in queries:
            result.append(prefix[left]^prefix[right+1])
        return result
            