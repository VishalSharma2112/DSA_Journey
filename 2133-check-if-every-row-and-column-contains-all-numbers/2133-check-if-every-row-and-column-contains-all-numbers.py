class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        
        for i in range(n):
            if len(set(matrix[i])) != n:
                return False
            
            col = set()
            for j in range(n):
                col.add(matrix[j][i])

            if len(col) != n:
                return False
        return True