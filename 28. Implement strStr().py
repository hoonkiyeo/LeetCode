class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        elif needle not in haystack:
            return -1
        elif needle in haystack:
            return haystack.index(needle)