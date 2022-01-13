class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        m = max(nums)

        if len(nums) < 3:
            return m
        else:
            nums.remove(m)
            second_m = max(nums)
            nums.remove(second_m)
            third_m = max(nums)
        return third_m
