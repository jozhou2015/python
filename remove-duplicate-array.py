class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup_count = 0
        length = len(nums)
        c = 1
        if len(nums) > 1 :
            prev = nums[0]
            for i in range(1,length):
                print(i, len(nums))
                if nums[i] != prev:
                    nums[c] = nums[i]
                    prev = nums[i]
                    c += 1
                    dup_count = 0
                else:
                    dup_count +=  1
                    if dup_count < 2:
                        nums[c] = nums[i]
                        prev = nums[i]
                        c += 1

            return c
        else:
            return length
a = [1,1,1]
print(Solution.removeDuplicates(a))
