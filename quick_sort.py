class Solution:
    def quicksort(s):
        left =[]
        equeal = []
        right = []
        if len(s) > 1:
            pivot = s[0]
            for x in s:
                if x < pivot:
                    left.append(x)
                if x  == pivot:
                    equeal.append(x)
                if x > pivot:
                    equeal.append(x)
            return Solution.quicksort(left) + equeal + Solution.quicksort(right)
        else:
            return s

s = input('input array')
l1 =[int(x) for x in s.split()]
print(Solution.quicksort(l1))


