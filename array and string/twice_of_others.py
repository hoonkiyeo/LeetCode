class Solution(object):
    def dominantIndex(self, nums):
        idx = nums.index(max(nums))
        largest = max(nums)
        is_twice = False

        if len(nums) < 2:
            return idx

        nums.pop(idx)
        for num in nums:
            if 2 * num <= largest:
                is_twice = True
            else:
                is_twice = False
                break

        return idx if is_twice else -1


