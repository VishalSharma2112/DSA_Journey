class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        def fastExp(a, b, m):
            if b==0:
                return 1
            
            half = fastExp(a, b//2, m)

            if b%2 == 0:
                return (half*half)%m
            else:
                return (a*half*half)%m
        
        for idx, i in enumerate(variables):
            a = i[0]
            b = i[1]
            c = i[2]
            m = i[3]
            inner = fastExp(a, b, 10)
            outer = fastExp(inner, c, m)
            if outer == target:
                ans.append(idx)
        return ans