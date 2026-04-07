# Решение ДП в данном случае не оптимально
"""class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[10**10] * k for j in range(n)]
        for i in range(k):
            for j in range(i*2, n):
                if i == 0 and j == 0:
                    dp[j][i] = nums[0]
                elif i == 0:
                    dp[j][i] = min(dp[j-1][i], nums[j])
                else:
                    dp[j][i] = min(dp[j-1][i], max(nums[j], dp[j-2][i-1])) 
        return (dp[-1][-1])"""

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums)
        mid = (l+r)//2
        while l+1 < r:
            if self.can_rob(nums, mid, k):
                r = mid
            else:
                l = mid
            mid = (l+r)//2
        if self.can_rob(nums, mid, k) and (mid in nums):
            return mid
        else:
            return mid+1
        
    def can_rob(self, nums, mid, k):
        i = 0
        while i < len(nums) and k > 0:
            if nums[i] <= mid:
                i += 2
                k -= 1
            else:
                i += 1
        return k==0