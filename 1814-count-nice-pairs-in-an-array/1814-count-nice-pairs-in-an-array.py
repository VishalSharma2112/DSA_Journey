import math
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        count_freq = {}
        answer = 0

        for i in nums:
            diff = i - int(str(i)[::-1])
            answer = (answer + count_freq.get(diff, 0)) % MOD
            count_freq[diff] = count_freq.get(diff, 0) + 1
        return answer