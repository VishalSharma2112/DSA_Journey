class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindromeCheck(i, j):
            while j>i:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        i, j = 0, len(s)-1
        while j > i:
            if s[i] != s[j]:
                return palindromeCheck(i+1, j) or palindromeCheck(i, j-1)
            i += 1
            j -= 1
        return True