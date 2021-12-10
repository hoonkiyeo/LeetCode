class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]== target:
                    output = [i,j]
        return output


sol = Solution()
print(sol.twoSum(nums = [2,7,11,15], target = 9))