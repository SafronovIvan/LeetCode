class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ' '
        s = s.strip()
        for i in s:
            if i in "-+" and ans[-1] in "+-":
                return 0
            elif i in "-+" and ans==" ":
                ans = i
            elif i in "0123456789":
                ans += i
            else:
                break
        if ans[0] == "+" or ans == "-":
            ans = ans[1:]
        if ans == " " or ans == "":
            ans = 0
        if int(ans) > 2**31-1:
            ans = 2**31-1
        if int(ans) < -2**31:
            ans = -2**31
        return int(ans)
        