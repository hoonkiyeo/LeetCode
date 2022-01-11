class Solution(object):
    def moveZeroes(self, nums):
        i = cnt = 0
        if len(nums) < 2:
            return nums
        else:
            while cnt < len(nums):
                if nums[i] == 0:
                    nums.append(nums.pop(i))
                else:
                    i += 1
                cnt += 1
        return nums