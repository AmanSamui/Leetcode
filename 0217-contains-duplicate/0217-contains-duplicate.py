class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set=set()
        l=0
        n=len(nums)
        for r in range(0,n):
            if nums[r] in hash_set:
                # l+=1
                return True
                break
            hash_set.add(nums[r])   
        return False
nums = [1,2,3,1]
# nums = [1,2,3,4]
# nums = [1,1,1,3,3,4,3,2,4,2]

obj=Solution()

print(obj.containsDuplicate(nums))
