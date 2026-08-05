class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        right=m+n-1
        while n>0:
            if m>0 and nums1[m-1] > nums2[n-1]:
                nums1[right]=nums1[m-1]
                m-=1
            else:
                nums1[right]=nums2[n-1]
                n-=1
            right-=1
        return nums1
obj=Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(obj.merge(nums1,m,nums2,n))