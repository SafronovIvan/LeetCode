class Solution:
    def tribonacci(self, n: int) -> int:
        t1, t2, t3 = 0, 1, 1
        if n < 1:
            return 0
        if n <= 2:
            return 1
        for i in range(n-2):
            t1, t2, t3 = t2, t3, t1+t2+t3
        return t3
        