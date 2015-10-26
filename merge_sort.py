class Solution:
    def mergeMedian(self,m,n):
        lenm = len(m)
        lenn = len(n)
        i, j, k = 0, 0, 0
        while i < lenn and j < lenm:
            if n[i] < m[j]:
                a[k] = n[i]
                i += 1
                k += 1
            else:
                a [k] = m[j]
                j += 1
                k += 1
        while i < lenn:
            a [k] = n[i]
            k += 1
            i += 1
        while j < lenm:
            a [k] = m[j]
            k += 1
            j += 1

