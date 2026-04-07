class Solution:
    def romanToInt(self, s: str) -> int:
        sl = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        for i in range(len(s)-1):
            if sl[s[i]] < sl[s[i+1]]:
                ans -= sl[s[i]]
            else:
                ans += sl[s[i]]
        ans += sl[s[-1]]
        return ans