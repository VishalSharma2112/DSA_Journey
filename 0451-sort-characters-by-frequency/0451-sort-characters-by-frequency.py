class Solution:
    def frequencySort(self, s: str) -> str:
        answer = ""
        char_freq = {}
        for i in s:
            char_freq[i] = char_freq.get(i, 0) + 1
        sorted_chars = sorted(char_freq.items(), key=lambda x:x[1], reverse=True)
        for i in sorted_chars:
            answer += i[0]*i[1]
        return answer