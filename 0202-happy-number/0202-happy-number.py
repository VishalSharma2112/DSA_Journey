class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()

        while(True):
            temp = 0
            while(n>0):
                temp = temp + (n%10)**2
                n //= 10
            if temp==1:
                return True
            else:
                if temp in results:
                    return False
                else:
                    results.add(temp)
                    n = temp
