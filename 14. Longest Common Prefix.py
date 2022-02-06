class Solution(object):
    def longestCommonPrefix(self, strs):
        size = len(strs)
        prefix = ""

        if not strs:
            return prefix
        elif size == 1:
            return strs[0]
        else:
            strs.sort()
            for x,y in zip(strs[0], strs[-1]):
                if x == y:
                    prefix += x
                else:
                    break
        return prefix