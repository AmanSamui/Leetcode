class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)

        k=0
        for i in range(0,n):
            if(nums[i] !=val):
                nums[k]=nums[i]
                k+=1
        return k
nums = [0,1,2,2,3,0,4,2]    
val=2
obj=Solution()
result=obj.removeElement(nums,val)
print("K:",result)
print("nums:",nums)