class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        i = 0
        count = 0
        vowel = {'a', 'i', 'o', 'u', 'e'}
        for j in range(len(s)):
            if s[j] in vowel:
                count += 1
            if j-i+1 == k:
                ans = max(ans, count)
                if s[i] in vowel:
                    count -= 1
                i += 1
        return(ans)