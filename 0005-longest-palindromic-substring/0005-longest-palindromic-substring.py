class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        MAX = 0
        st = 0
        start, end = 0, 0

        for i in range(n):
            length = 0  
            
            # ODD
            start = i
            end = i

            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1

            length = end - start - 1
            if length > MAX:
                MAX = length
                st = start+1

            # EVEN
            start = i
            end = i+1
            
            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
            
            length = end - start - 1
            if length > MAX:
                MAX = length
                st = start+1
    
        return s[st:st+MAX]