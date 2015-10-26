class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = self.quicksort(nums)
        return s[k-1]


    def quicksort(self,nums):
        less = []
        equeal = []
        greater = []
        n =  len(nums)
        if n > 1:
            pivot = nums[0]
            for i in range(n):
                if nums[i] > pivot:
                    less.append(nums[i])
                if nums[i] == pivot:
                    equeal.append(nums[i])
                if nums[i] < pivot:
                    greater.append(nums[i])
            return self.quicksort(less) + equeal + self.quicksort(greater)
        else:
            return nums

s1 = Solution()
s = input('input array')
l1 =[int(x) for x in s.split()]
print(s1.findKthLargest(l1,4))
