class Solution:
    def mySqrt(self, x: int) -> int:
        def squareRt(low, high):
            mid = (high+low)//2

            if mid*mid == x:
                return mid
            if low > high:
                return high

            if mid*mid < x:
                return squareRt(mid+1, high)
            else:
                return squareRt(low, mid-1)
        
        return squareRt(1, x)