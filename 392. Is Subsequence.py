class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        if len(t)<len(s):
            return False
        for i in range(len(s)):
            print(k, t)
            while t[k]!= s[i]:
                k += 1
                if k >= len(t):
                    break
            if i == len(s)-1 and k < len(t):
                return True
            k += 1
            if k >= len(t):
                break
            
        else:
            return True
        return False
        