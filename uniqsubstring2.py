class solution:
def uniqstring(self, s):
    cdict = {}
    ans = []
    string_seg=''
    for x in s:
        t =cdict.get(x,None)
        if t is None:
            string_seg = string_seg+x
            cdict[x] = 1
        else:
            if len(string_seg) > len(ans):
                ans = string_seg[:]
    return ans
