# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        if n == 1:
            return n
        else:
            left, right = 0, n
            while True:
                mid = left + (right - left) // 2
                guess_num = guess(mid)

                if guess_num == 0:
                    break
                elif guess_num == 1:
                    left = mid + 1
                else:
                    right = mid - 1

        return mid