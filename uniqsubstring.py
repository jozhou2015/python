s = input("input your string:\n")
x, x1 = 0,0
ans =[]
if len(s) == 1:
   ans = s
else:
    for x in range(len(s)):
        string_seg = s [x1:x+1]
        print(x,string_seg, ans)
        if len(set(string_seg)) != len(string_seg):
            print(ans, string_seg)
            if len(string_seg) > len(ans):
                ans = string_seg[:-1]
                x1 = x


print("answer is ",ans)




