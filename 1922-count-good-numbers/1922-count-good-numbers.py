class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def fastExp(a, b):
            if b == 0:
                return 1

            half = fastExp(a, b // 2)

            if b % 2 == 0:
                return (half * half) % MOD
            else:
                return (a * half * half) % MOD

        if n%2 == 0:
            return fastExp(20, n//2)
        else:
            return (5*fastExp(20, n//2)) % MOD