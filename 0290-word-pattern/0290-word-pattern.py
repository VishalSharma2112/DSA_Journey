class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words): return False
        maps_t = {}
        mapt_s = {}

        for i, j in zip(pattern, words):
            if i in maps_t:
                if maps_t[i] != j:
                    return False
            else:
                maps_t[i] = j

            if j in mapt_s:
                if mapt_s[j] != i:
                    return False
            else:
                mapt_s[j] = i

        return True