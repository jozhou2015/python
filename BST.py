class fb:
    def fbrecuresive(self,n):
        if n == 1:
            return 1
        return n * self.fbrecuresive(n-1)

fb1 = fb()
n = input(" input your number:\n")
print(fb1.fbrecuresive(int(n)))
