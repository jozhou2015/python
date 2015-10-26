class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(nums, target):
        d = dict()
        for x in range(len(nums)):
            d[x] = nums[x]
        for x in range(len(nums)):
            if target-nums[x] in d:
                return (x+1, d[target-nums[x]]+1)

if __name__ == '__main__':
    y = [3,2,4]
    sum = 6
    print(Solution.twoSum(y,sum))