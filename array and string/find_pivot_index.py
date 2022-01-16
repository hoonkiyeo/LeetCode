class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0
        size = len(nums)

        for i in range(size):
            if left_sum == total - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1