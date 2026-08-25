class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        temp = k
        num_set = set()
        for i in nums:
            if i%k==0:
                num_set.add(i)
        while(True):
            if k in num_set:
                k += temp
            else:
                break
        return k