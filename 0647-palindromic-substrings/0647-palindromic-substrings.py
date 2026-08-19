class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        def palinCheck(start, end) -> int:
            count = 0
            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
                count += 1
            return count

        for i in range(n):
            count += palinCheck(i, i)
            count += palinCheck(i, i+1)

            
        return count 