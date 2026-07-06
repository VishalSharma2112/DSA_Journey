from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        answer  = []
        for i in strs:
            sorted_str = ''.join(sorted(i))
            anagrams[sorted_str].append(i)
        
        for i in anagrams.keys():
            answer.append(anagrams[i])
        
        return answer