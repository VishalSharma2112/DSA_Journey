class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        freq_maps = {}
        left = 0
        max_count = 0

        for right in range(len(s)):
            freq_maps[s[right]] = freq_maps.get(s[right], 0)+1

            while freq_maps[s[right]] > 1:

                freq_maps[s[left]] -= 1
                if freq_maps[s[left]] == 0:
                    del freq_maps[s[left]]

                left += 1
            max_count = max(max_count, right-left+1)
        return(max_count)