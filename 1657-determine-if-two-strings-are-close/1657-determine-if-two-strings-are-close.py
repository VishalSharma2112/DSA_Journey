class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        map_word1 = {}
        map_word2 = {}

        for w1, w2 in zip(word1, word2):
            map_word1[w1] = map_word1.get(w1, 0)+1
            map_word2[w2] = map_word2.get(w2, 0)+1

        list1 = sorted(list(map_word1.values()))
        list2 = sorted(list(map_word2.values()))

        return (
            set(map_word1.keys())==set(map_word2.keys()) and
            list1 == list2
        )