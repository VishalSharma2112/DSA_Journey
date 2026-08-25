class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        count = 0
        Sum = 0

        for right in range(len(arr)):
            Sum += arr[right]
            if right-left+1 == k:
                if Sum >= threshold*k:
                    count += 1
                Sum -= arr[left]
                left += 1
        return count