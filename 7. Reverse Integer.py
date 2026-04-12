class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        zn = x//abs(x)
        ans = int(str(abs(x))[::-1])*zn
        if ans >= (2**31)-1 or ans <= -2**31+1:
            return 0
        return ans
        