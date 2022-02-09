class Solution(object):
    def reverse(self, x):
        reversed = int(str(abs(x))[::-1])

        if x > 0:
            if reversed > 2147483647:
                return 0
            return reversed
        else:
            if reversed > 2147483648:
                return 0
            return -reversed