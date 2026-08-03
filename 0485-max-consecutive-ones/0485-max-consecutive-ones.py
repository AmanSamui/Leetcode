class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        count=0
        maxi=0

        for i in range(0,n):
            if(nums[i]==1):
                count+=1
            else:
                count=0
            maxi=max(maxi,count)
        return maxi
# nums = [1, 1, 0, 0, 1, 1, 1, 0]
# nums = [0, 0, 0, 0, 0, 0, 0, 0]
nums = [1,1,0,1,1,1]
obj=Solution()
print(obj.findMaxConsecutiveOnes(nums))
