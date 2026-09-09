class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = -1
        maps = {}
        max_freq = 0

        for right in range(len(s)):
            maps[s[right]] = maps.get(s[right], 0)+1
            max_freq = max(max_freq, maps[s[right]])

            while (right-left+1) - max_freq > k:
                maps[s[left]] -= 1

                if maps[s[left]] == 0:
                    del maps[s[left]]
                
                left += 1

            ans = max(right-left+1, ans)
        return(ans)