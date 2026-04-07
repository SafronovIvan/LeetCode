class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st = set()
        for i in nums:
            if i not in st:
                st.add(target-i)
            else:
                a = nums.index(target-i)
                return [a, nums[a+1:].index(i)+a+1]