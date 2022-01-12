class Solution(object):
    def heightChecker(self, heights):
        cnt = 0
        expected = sorted(heights)
        for item in zip(heights, expected):
            if item[0] != item[1]:
                cnt += 1

        return cnt