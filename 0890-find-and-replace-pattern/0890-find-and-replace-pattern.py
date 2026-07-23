class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer = []
        pattern_map = {}
        num_pattern = 1
        for i in pattern:
            if i not in pattern_map:
                pattern_map[i] = num_pattern
                num_pattern += 1
        numerical_pattern = 0
        for i in pattern:
            numerical_pattern = numerical_pattern*10 + pattern_map[i]

        for word in words:
            temp = {}
            index = 1
            for alpha in word:
                if alpha not in temp:
                    temp[alpha] = index
                    index += 1
            temp_num_pattern = 0
            for alpha in word:
                temp_num_pattern = temp_num_pattern*10 + temp[alpha]
            if temp_num_pattern == numerical_pattern:
                answer.append(word)
        return answer