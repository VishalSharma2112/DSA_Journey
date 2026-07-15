class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        freq_set = set()

        for i in nums:
            freq_set.add(i)
        longest = 0
        for i in freq_set:
            if i-1 not in freq_set:
                current = i
                chain = 1

                while current+1 in freq_set:
                    current+=1
                    chain += 1

                longest = max(longest, chain)

        return longest