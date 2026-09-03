class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        string = str(num)
        left = 0
        window_num = 0
        count = 0
        for right in range(len(string)):

            if right-left+1 == k:
                window_num = int(string[left:right+1])
                if window_num!=0 and num%window_num == 0:
                    count += 1
                left+=1

        return(count)