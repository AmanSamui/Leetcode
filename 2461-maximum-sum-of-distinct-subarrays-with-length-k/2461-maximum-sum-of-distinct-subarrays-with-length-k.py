class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxi=0
        # count= defaultdict(int)
        fre_map={}
        cur_sum=0
        l=0
        for r in range(len(nums)):
            cur_sum+=nums[r]
            fre_map[nums[r]] =fre_map.get(nums[r],0)+1

            if r-l+1>k:
                fre_map[nums[l]]-=1
                if fre_map[nums[l]]==0:
                    fre_map.pop(nums[l])
                cur_sum-=nums[l]
                l+=1

            if len(fre_map)==k and r-l+1==k:
                maxi=max(maxi,cur_sum)

        return maxi


obj=Solution()

nums = [1,5,4,2,9,9,9]
k=3
print(obj.maximumSubarraySum(nums,k))