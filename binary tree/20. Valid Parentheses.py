class Solution(object):
    def isValid(self, s):
        if len(s) < 2:
            return False
        else:
            stack = []
            mapping = {"(":")", "[":"]", "{":"}"}
            closing = [")", "]", "}"]

            for letter in s:
                if s in mapping:
                    stack.append(s)
                elif s in closing:
                    if len(stack) != 0:
                        if s == mapping[stack[-1]]:
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
            return len(stack) == 0
