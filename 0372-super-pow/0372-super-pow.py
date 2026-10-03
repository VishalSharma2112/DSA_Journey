class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        if a == 1:
            return 1
        exponent = 0
        for i in b:
            exponent = (exponent*10 + i) % 1140
            if exponent == 0:
                exponent = 1140
        
        def fastExpo(a, b):
            if b==0:
                return 1

            if b%2 == 0:
                return fastExpo(a*a, b//2)%1337
            else:
                return (a*fastExpo(a, b-1))%1337
        
        return fastExpo(a, exponent)