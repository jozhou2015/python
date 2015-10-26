class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cdict = {}
        ans = 1
        string_len = 0
        if not s:
            return 0
        for x in s:
            t = cdict.get(x,None)
            if t is not None:
                cdict = {}
                if string_len > ans:
                    ans = string_len
                string_len = 1
            else:
                cdict[x] = 1
                string_len += 1
        if string_len > ans:
            ans = string_len
        return ans