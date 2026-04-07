"""class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sl = {}
        ans = 0
        count = 0
        for i in range(len(s)):
            if s[i] not in sl:
                sl[s[i]] = i
                count += 1
            else:
                ans = max([ans, i-sl[s[i]], count])
                count = i-sl[s[i]]
                sl_keys = list(sl.keys())
                for j in sl_keys:
                    if sl[j] < sl[s[i]]:
                        del sl[j]
                sl[s[i]] = i
        if ans == 0:
            return len(sl)
        return max([ans, count])"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sl = {}
        ans = 0
        count = 0
        last = 0
        for i in range(len(s)):
            if s[i] not in sl:
                sl[s[i]] = i
                count += 1
                ans = max(ans, 1)
            else:
                last = max(last,sl[s[i]])
                ans = max([ans, i-last, count])
                count = i-last
                sl[s[i]] = i
        return max(ans, count)


        
