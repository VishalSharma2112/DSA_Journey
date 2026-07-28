class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        double = set()
        for i in arr:
            if i==0 and i in double:
                return True
            if i not in double:
                double.add(i)
        for i in arr:
            if i*2 in double and i!=0:
                return True
        return False