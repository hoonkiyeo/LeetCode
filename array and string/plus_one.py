class Solution(object):
    def plusOne(self, digits):
        res = 0
        for i in digits:
            res = res * 10 + i
        res = res + 1
        return str(res)