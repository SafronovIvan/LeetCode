class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = []
        nums1.append(10**10)
        nums2.append(10**10)
        n1 = nums1[:]
        n2 = nums2[:]
        s_n = len(nums1)+len(nums2)
        for i in range((len(nums1)+len(nums2))//2):
            if nums1[0] > nums2[0]:
                num.append(nums2[0])
                del nums2[0]
            else:
                num.append(nums1[0])
                del nums1[0]
        if (s_n)%2==0:
            return (num[(s_n-2)//2] + num[(s_n-2)//2-1])/2
        else:
            return num[(len(n1)+len(n2)-2)//2]