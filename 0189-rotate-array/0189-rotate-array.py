class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        nums[:]=nums[n-k:n]+nums[0:n-k]
        return nums

# nums = [1, 2, 3, 4, 5, 6]
nums = [1,2,3,4,5,6,7]

k=3
obj=Solution()
print(obj.rotate(nums,k))