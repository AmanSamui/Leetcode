class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(0,n):
            ans.append(nums[i])
        for i in range(0,n):
            ans.append(nums[i])
        return ans


obj=Solution()

# nums = [1,3,2,1]
nums = [1,2,1]

print(obj.getConcatenation(nums))