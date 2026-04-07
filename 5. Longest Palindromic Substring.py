class Solution:
    def longestPalindrome(self, s: str) -> str:
        sp = []
        ans = 0
        ans_st = ""
        if len(s)==1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        s = " "+s+" "
        for i in range(1, len(s)-1):
            for j in range(len(sp)-1, -1, -1):
                if sp[j] < 0:
                    del sp[j]
                    if i > ans:
                        ans = i+1
                        ans_st = s[:i]
                    continue
                if s[i] == s[sp[j]]:
                    if (i-sp[j])%2==0:
                        if i-sp[j]+1 >= ans:
                            ans = i-sp[j]+1
                            ans_st = s[sp[j]:i+1]
                    else:
                        if i-sp[j]+1 >= ans:
                            ans = i-sp[j]+1
                            ans_st = s[sp[j]:i+1]
                    sp[j]-=1
                else:
                    if (i-sp[j])%2==0:
                        if i-sp[j]-1 >= ans:
                            ans = i-sp[j]-1
                            ans_st = s[sp[j]+1:i]
                    else:
                        if i-sp[j]-1 >= ans:
                            ans = i-sp[j]-1
                            ans_st = s[sp[j]+1:i]
                    del sp[j]
            if s[i+1] == s[i-1]:
                sp.append(i-1)
            if s[i+1] == s[i]:
                sp.append(i)
        if ans_st == "":
            return s[1]
        return ans_st
            
