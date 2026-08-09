class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s:
            if i.isalnum():
                word += i.lower()
        
        i = 0
        j = len(word)-1

        while j>i:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True