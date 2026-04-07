class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        if numRows == 1:
            return s
        for i in range(numRows):
            for j in range(0,len(s), (numRows-1)*2):
                if i == 0:
                    ans += s[j]
                elif i == numRows-1:
                    if j+numRows-1 < len(s):
                        ans += s[j+numRows-1]
                else:
                    if j+i < len(s):
                        ans += s[j+i]
                    if j + (numRows-1)*2-i < len(s):
                        ans += s[j + (numRows-1)*2-i]
            print(i, ans)
        return ans