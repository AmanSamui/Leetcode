class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length=len(nums)
        arr=[]
        for i in range(0,n):
            arr.append(nums[i])
            arr.append(nums[i+n])
        return arr
obj=Solution()

# nums = [2,5,1,3,4,7]
# n = 3

nums = [1,2,3,4,4,3,2,1]
n = 4
print(obj.shuffle(nums,n))