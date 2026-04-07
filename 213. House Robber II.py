class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) >1:
            nums2 = [0, 0, 0]+nums[:-1]+[0, 0, 0]
            sp = [0]*len(nums2)
            for i in range(3, len(sp)):
                sp[i] = max(sp[i-2],sp[i-3])+nums2[i]
            ans1= max(sp)
            nums3 = [0, 0, 0]+nums[1:]+[0, 0, 0]
            sp = [0]*len(nums3)
            for i in range(3, len(sp)):
                sp[i] = max(sp[i-2],sp[i-3])+nums3[i]
            ans2= max(sp)
            return max(ans1, ans2)
        else:
            return nums[0]