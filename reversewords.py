class Solution(object):
    def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        # c =''
        # e = list()
        # if len(s) <1:
        #     return s
        # for word in  s[::-1].split():
        #     c = word[::-1]
        #     e.append(c)
        # f = " ".join(e)


        return ' '.join([word[::-1] for word in s[::-1].split()])
s = input('input a string:')
rever = Solution.reverseWords(s)
print(rever)