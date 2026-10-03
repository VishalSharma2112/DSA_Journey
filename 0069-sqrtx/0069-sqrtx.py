class Solution:
    def mySqrt(self, x: int) -> int:
        def squareRt(low, high, num):
            mid = (high+low)//2

            if mid*mid == num:
                return mid
            if low > high:
                return high

            if mid*mid < num:
                return squareRt(mid+1, high, num)
            else:
                return squareRt(low, mid-1, num)
        
        return squareRt(1, x, x)