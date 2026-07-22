class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alpha_freq = {}

        for i in t:
            alpha_freq[i] = alpha_freq.get(i, 0)+1
        for i in s:
            alpha_freq[i] -= 1
        for i in alpha_freq:
            if alpha_freq[i] == 1:
                return i