class Solution:
    def rotate(self,numbers,k):
        n = len(numbers)
        if n < 2:
            return numbers
        for i in range(k/2):
            temp = numbers[i]
            numbers[i] = numbers[k-i]
            numbers[k-i] = temp
        for j in range(k,(n-k)/2,1):
            temp = numbers[j]
            numbers[j] =

