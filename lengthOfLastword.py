class Solution:
    def lenOfLastWord(s):
        x = len(s)
        if x < 1:
            return 0
        l = 0
        flag = 1
        pre = s[-1]
        if s[-1] == ' ':
            flag = -1
        for i in range(x):
            print(s[-i],"\n")
            if flag > 0:
                if s[-i-1] == " ":
                    return l
                l += 1
            else:
                if s[-i-1] != pre:
                    print(flag)
                    flag = 1
                    l +=1
        return l



s = input('input string')
print (Solution.lenOfLastWord(s))

