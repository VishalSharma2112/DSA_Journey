class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer = []

        for word in words:
            W2P = {}
            P2W = {}
            result = True
            for w, p in zip(word, pattern):
                if w in W2P and W2P[w] != p:
                    result = False
                    break
                if p in P2W and P2W[p] != w:
                    result = False
                    break
                W2P[w] = p
                P2W[p] = w
            if result:
                answer.append(word)
        return answer
                    