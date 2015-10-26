class Solution:
    def permutation(self,s):
        if len(s) < 2:
            yield s
        l = list()
        for i in range(len(s)):
            x = s[i]
            xz = s[:i] + s[i+1:]
            for p in self.permutation(xz):
                yield ([x]+p)



s =  input('input string')
li = list(s)
#print(li)
s1 = Solution()
for p in s1.permutation(li):
    print(p)


