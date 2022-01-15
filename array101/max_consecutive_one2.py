class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        is_zero = False
        size = len(nums)
        curr_cons = prev_cons = max_cons = 0

        for num in nums:
            if num == 1:
                curr_cons += 1
            else:
                is_zero = True
                max_cons = max(max_cons, curr_cons + prev_cons + 1)
                prev_cons = curr_cons
                curr_cons = 0
        max_cons = max(max_cons, curr_cons + prev_cons + 1)

        return size if not is_zero else max_cons
