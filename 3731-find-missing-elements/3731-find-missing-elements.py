class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        smallest=nums[0]
        largest=0
        arr=[]
        for i in range(0,n):
            smallest=min(smallest,nums[i])
            largest=max(largest,nums[i])
        # return smallest,largest

        for i in range(smallest,largest+1):
             arr.append(i)
        # return arr
        # l=len(arr)
        missing=[]
        for i in range(smallest,largest+1):
            if i not in nums:
                missing.append(i)

            # missing.append(i)
           
        return missing
                    

        
# nums = [1,4,2,5]
nums = [7,8,6,9]
obj=Solution()
print(obj.findMissingElements(nums))