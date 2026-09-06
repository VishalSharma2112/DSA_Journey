class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, b, c = 0, 0, 0

        left = 0
        count = 0
        n = len(s)

        for right in range(n):
            if s[right] == 'a':
                a += 1
            elif s[right] == 'b':
                b += 1
            else:
                c += 1

            while a>=1 and b>=1 and c>=1:
                count += n-right

                if s[left] == 'a':
                    a -= 1
                elif s[left] == 'b':
                    b -= 1
                else:
                    c -= 1
                left += 1
        return(count)