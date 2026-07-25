class Solution:
    def maxProduct(self, n: int) -> int:
        list_nums = []
        length = len(str(n))
        for i in range(length):
            list_nums.append(n%10)
            n //= 10
        sorted_list = sorted(list_nums)
        return sorted_list[length-1]*sorted_list[length-2]