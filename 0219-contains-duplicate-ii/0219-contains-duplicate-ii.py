class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # n=len(nums)

        # for i in range(0,n-1):
        #     for j in range(i+1,n):
        #         if nums [i]==nums[j] and abs(i-j)<=k:
        #             return True
        #             break
                
        # return False
        window=set()
        l=0
        for r in range(len(nums)):

            if r-l>k:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False



obj=Solution()
nums = [1,2,3,1]
k = 3

# nums = [1,0,1,1]
# k = 1

# nums = [1,2,3,1,2,3]
# k = 2
print(obj.containsNearbyDuplicate(nums,k))