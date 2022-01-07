class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j] * 2 or arr[j] == arr[i] * 2:
                    return True

        return False