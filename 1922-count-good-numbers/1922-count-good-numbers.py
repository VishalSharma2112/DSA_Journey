class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def fastExp(a, n):
            result = 1
            while n:
                if n%2 != 0:
                    result = (a*result)%MOD
                
                a = (a*a) % MOD
                n = n//2
            return result

        if n%2 == 0:
            return fastExp(20, n//2)
        else:
            return (5*fastExp(20, n//2)) % MOD