class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        lists = list(s)
        while j > i:
            if lists[i] not in vowels:
                i+=1
            elif lists[j] not in vowels:
                j-=1
            else:
                lists[i], lists[j] = lists[j], lists[i]
                i += 1
                j -= 1
        return ''.join(lists)