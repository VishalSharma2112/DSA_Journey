# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)//2
        count = 0
        for i in nums:
            if count == 0:
                element = i
                count += 1
            elif element != i:
                count -= 1
            else:
                count +=1
        return element