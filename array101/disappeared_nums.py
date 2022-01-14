class Solution(object):
    def findDisappearedNumbers(self, nums):

        dic = {}
        result = []

        for num in nums:
            dic[num] = 1

        for i in range(1, len(nums) + 1):
            if i not in dic:
                result.append(i)
        return result



