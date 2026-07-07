class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_ran = {}
        map_mag = {}

        for i in ransomNote:
            map_ran[i] = map_ran.get(i, 0) + 1

        for i in magazine:
            map_mag[i] = map_mag.get(i, 0) + 1

        for i in map_ran:
            if i not in map_mag:
                return False
            if map_ran[i] > map_mag[i]:
                return False
        return True
                
      