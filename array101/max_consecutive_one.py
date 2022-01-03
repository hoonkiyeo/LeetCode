class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        self.count = 0
        self.maxcount = 0

        for num in nums:
            if num == 1:
                self.count += 1
            else:
                self.maxcount = max(self.maxcount, self.count)
                self.count = 0

        return max(self.count, self.maxcount)