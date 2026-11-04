class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nextgreater = [0]*len(nums2)
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            while(len(stack)!=0 and nums2[i]>=stack[-1]):
                stack.pop()
            if len(stack)!=0:
                nextgreater[i] = stack[-1]
            else:
                nextgreater[i] = -1
            stack.append(nums2[i])
        ans = []
        for i in nums1:
            for index, j in enumerate(nums2):
                if i==j:
                    ans.append(nextgreater[index])
        return ans

            