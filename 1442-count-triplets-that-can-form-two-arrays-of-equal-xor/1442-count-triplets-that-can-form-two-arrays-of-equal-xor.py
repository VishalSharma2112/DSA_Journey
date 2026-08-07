class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        output = 0
        for i in range(len(arr)):
            XOR1 = 0
            for j in range(i+1, len(arr)):
                XOR1 ^= arr[j-1]
                XOR2 = 0
                for k in range(j, len(arr)):
                    XOR2 ^= arr[k]
                    if XOR1 == XOR2:
                        output += 1
        return output