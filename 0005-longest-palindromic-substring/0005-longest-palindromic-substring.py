class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        MAX = ""
        st = 0
        start, end = 0, 0

        def palinCheck(start, end) -> str:
            while start>=0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
            
            return s[start+1 : end]

        for i in range(n):
            # ODD
            odd = palinCheck(i, i)
            if len(odd) > len(MAX):
                MAX = odd
            # EVEN
            even = palinCheck(i, i+1)
            if len(even) > len(MAX):
                MAX = even

        return MAX