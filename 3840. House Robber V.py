class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        nums = [0, 0, 0]+nums+[0, 0, 0]
        colors = [0, 0, 0]+colors+[0, 0, 0]
        sp = [0]*len(nums)
        for i in range(3, len(sp)):
            if colors[i] == colors[i-1]:
                sp[i] = max(sp[i-2],sp[i-3])+nums[i]
            else:
                sp[i] = max(sp[i-2],sp[i-3], sp[i-1])+nums[i]
        return max(sp)