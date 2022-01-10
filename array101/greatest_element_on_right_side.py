class Solution(object):
    def replaceElements(self, arr):
        if len(arr) < 2:
            arr[0] = -1
            return arr
        else:
            for i in range(len(arr)-1):
                arr[i] = max(arr[i+1:])
            arr[-1] = -1

        return arr