class Solution(object):
    def removeElement(self, nums, val):

        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)

        return len(nums)