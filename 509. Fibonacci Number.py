class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        a = 1
        b = 1
        c = 0
        for i in range(n-1):
            c = a+b
            b = a
            a = c
        return (b)