class Solution(object):
    def validMountainArray(self, arr):
        size = len(arr)
        i = 0
        j = size -1
        idx = arr.index(max(arr))

        if size < 3:
            return False
        elif idx == 0 or arr[idx] == arr[-1]:
            return False
        elif arr[0] > arr[1] or arr[-2] < arr[-1]:
            return False
        else:
            while True:
                if arr[i+1] > arr[i]:
                    i += 1
                elif arr[j-1] > arr[j]:
                    j -= 1
                else:
                    break
                if i >= j:
                    break
        if i == j and i != 0 and j != len(arr) -1:
            return True
        else:
            return False