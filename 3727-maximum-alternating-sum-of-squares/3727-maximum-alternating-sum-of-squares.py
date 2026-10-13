class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]*nums[0]
        
        sorted_num = []
        for i in nums:
            sorted_num.append(abs(i))
        sorted_num.sort()
        ans = 0
        i = 0
        j = len(sorted_num)-1
        while i<=j:
            if i==j:
                ans += sorted_num[j]*sorted_num[j]
                break
            ans += (sorted_num[j]*sorted_num[j]) - (sorted_num[i]*sorted_num[i])
            i += 1
            j -= 1
        return(ans)
