class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0, 0, 0]+nums+[0, 0, 0]
        sp = [0]*len(nums)
        for i in range(3, len(sp)):
            sp[i] = max(sp[i-2],sp[i-3])+nums[i]
        return max(sp)