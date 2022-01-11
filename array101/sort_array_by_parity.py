class Solution(object):
    def sortArrayByParity(self, nums):
        if len(nums) < 2:
            return nums
        else:
            i = cnt = 0
            while cnt < len(nums):
                if nums[i] % 2 != 0:
                    nums.append(nums.pop(i))
                else:
                    i += 1
                cnt += 1
        return nums
