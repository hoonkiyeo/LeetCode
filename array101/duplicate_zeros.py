class Solution(object):
    def duplicateZeros(self, arr):
        if not 0 in arr:
            return arr
        else:
            size = len(arr)
            index = 0
            while True:
                if arr[index] == 0:
                    arr.pop(-1)
                    arr.insert(index+1, 0)
                    index += 2
                elif arr[index] != 0:
                    index += 1
                if index >= size:
                    break
        return arr
