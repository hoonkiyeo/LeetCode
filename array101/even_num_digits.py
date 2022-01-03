class Solution(object):
    def findNumbers(self, nums):
        self.count = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                self.count += 1
            else:
                continue

        return self.count