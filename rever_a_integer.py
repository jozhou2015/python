class Solution:
    def revInteger(x):
        flag = 1
        if x < 0:
            flag = -1
            x = abs(x)
        s = 0
        while x  > 0:
            print(x)
            s = s*10 + x % 10
            x = int(x/10)
        return s*flag

s = int(input('input:'))
print(Solution.revInteger(s))

