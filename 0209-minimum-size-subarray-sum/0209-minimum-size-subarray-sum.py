class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        mini=float('inf')
        sum=0
        i=0
        j=0
        while j<len(nums):
            sum+=nums[j]
            while sum>=target:
                mini=min(mini,j-i+1)
                sum-=nums[i]
                i+=1
            j+=1

        if mini==float('inf'):
            return 0
        return mini
obj=Solution()
# target = 7
# nums = [2,3,1,2,4,3]
# target = 4
# nums = [1,4,4]
target = 11
nums = [1,1,1,1,1,1,1,1]
print(obj.minSubArrayLen(target,nums))

