class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)
        else:
            for i in ragne(len(nums)-1, 0, -1):
                if nums[i] == nums[i-1]:
                    del nums[i]

        return len(nums)


