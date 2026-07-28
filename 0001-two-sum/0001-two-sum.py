class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        # i=0;
        for i in range(0,n-1):
            for j in range(1,n):
                if(nums[i]+nums[j]==target and i!=j):
                    return i,j
                    break
            



obj=Solution()
nums = [3,2,3]
result=obj.twoSum(nums,6)
print(result)