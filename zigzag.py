class Solution(object):
    def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) < numRows:
            return s
        zigzag = ['' for x in range(numRows)]
        row, step = 0, 1
        for c in s:
            zigzag[row] += c
            if row == 0:
                step = 1
            elif row == numRows-1:
                step = -1
            row += step
        
        print(zigzag)
        return ''.join(zigzag)

s='ab'
d = Solution.convert(s,1)
print(d)