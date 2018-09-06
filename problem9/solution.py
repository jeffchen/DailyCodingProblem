'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''
def maximunOfNonAdjacentNum(arr):
    if len(arr) == 1:
        return arr[0]

    # [2]
    maxSum = [arr[0]]
    # [2, 4] -> 4 is bigger -> [2, 4]
    maxSum.append(getBigNum(maxSum[0], arr[1]))

    # first round: [2 + 6 = 8, 4] -> 8 is bigger -> [2, 4, 8]
    # secound round: [4 + 2 = 6, 8] -> 8 is bigger -> [2, 4, 8, 8]
    # thirs round: [8 + 5 = 13, 8] -> 13 is bigger -> [2, 4, 8, 8, 13]
    # return 13
    for i in xrange(2, len(arr)):
        maxSum.append(getBigNum(maxSum[i - 2] + arr[i], maxSum[i - 1]))

    return maxSum[-1]

def getBigNum(val1, val2):
    return val1 if val1 > val2 else val2

inputArr = [2, 4, 6, 2, 5]
print maximunOfNonAdjacentNum(inputArr)
