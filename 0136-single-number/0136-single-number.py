class Solution(object):
    def singleNumber(self, nums):
        #your code goes here
        n=len(nums)
        hash_map={}
        for num in nums:
            hash_map[num]=hash_map.get(num,0)+1
        for key in hash_map:
            if(hash_map[key]==1):
                return key

# nums = [1, 2, 2, 4, 3, 1, 4]
# nums = [5]
# nums = [2,2,1]
nums = [4,1,2,1,2]
obj=Solution()
print(obj.singleNumber(nums))
   