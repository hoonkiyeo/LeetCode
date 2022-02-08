from collections import deque


class Solution(object):
    def letterCombinations(self, digits):
        mapping = {"1": "", "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                   "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        ans = []
        if not digits:
            return ans
        elif len(digits) == 1:
            return mapping[digits]
        else:
            for i in range(len(digits)):
                ans.append(mapping[digits[i]])

            while len(ans) > 1:
                l1 = ans.pop()
                l2 = ans.pop()

                comb = []
                for i in l1:
                    for j in l2:
                        comb.append(j + i)
                ans.append(comb)
            final_comb = ans[0]

        return final_comb
