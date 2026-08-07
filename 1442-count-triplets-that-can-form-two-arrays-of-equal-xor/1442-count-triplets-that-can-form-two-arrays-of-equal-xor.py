class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        output = 0
        for i in range(len(arr)):
            XOR = 0
            for k in range(i, len(arr)):
                XOR ^= arr[k]
                if XOR == 0:
                    output += k-i
        return output
