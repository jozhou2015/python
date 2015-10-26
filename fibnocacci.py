class Fibnoccai:
    def fib(self,n):
       if n == 0:
           return 0
       if n == 1: return 1
       return self.fib(n-1) + self.fib(n-2)

f = Fibnoccai()
n = input('input your number:\n')
print(f.fib(int(n)))