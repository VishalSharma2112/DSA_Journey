class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        newArr = nums+nums
        stack = []
        for i in range(len(newArr)-1, -1, -1):
            while(len(stack)!=0 and newArr[i] >= stack[-1]):
                stack.pop()
            if len(stack)==0:
                stack.append(newArr[i])
                newArr[i] = -1
            else:
                temp = newArr[i]
                newArr[i] = stack[-1]
                stack.append(temp)
        return newArr[0:len(nums)]