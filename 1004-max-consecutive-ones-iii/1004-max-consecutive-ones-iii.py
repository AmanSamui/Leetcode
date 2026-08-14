class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen=0
        l=0
        r=0
        zeros=0
        n=len(nums)
        while r<n:

            if nums[r] ==0:
                zeros+=1
            while zeros>k:

                if nums[l] ==0:
                    zeros-=1
                l+=1
            if zeros<=k:
                length=r-l+1
                maxlen=max(maxlen,length)
            r+=1
        return maxlen

# nums=[1,1,1,0,0,0,1,1,1,1,0]
# k = 2

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3


obj=Solution()
print(obj.longestOnes(nums,k))