class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        answer = []

        l1 = len(str(low))
        l2 = len(str(high))

        digits = "123456789"

        for i in range(l1, l2 + 1):
            for j in range(10 - i):
                string_num = digits[j:j + i]
                num = int(string_num)

                if low <= num <= high:
                    answer.append(num)

        return answer