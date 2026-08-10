class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi=float('-inf')
        sum=0
        n=len(nums)

        l=0
        for r in range(0,k):
            sum+=nums[r]

        maxi=max(maxi,sum)
        r=k
        # print(nums[r])

        while r<n:
            sum+=nums[r]
            sum-=nums[l]

            l+=1
            r+=1
            maxi=max(maxi,sum)
        return maxi/k

            
obj=Solution()
# nums = [1,12,-5,-6,50,3]
# k = 4
nums = [-1]
k = 1

print(obj.findMaxAverage(nums,k))

