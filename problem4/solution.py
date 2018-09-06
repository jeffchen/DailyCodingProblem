'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''
def findMissingInteger(arr):
    tmpArr = list(arr)
    # let tmpArr[arr[i]] = arr[i] -> [3, 1, -1, 3]
    for x in arr:
        if x >= 0 and x < len(arr):
            tmpArr[x] = x

    # find first tmpArr[i] != i, or every elements are bigger than len(arr)
    for i in xrange(1, len(tmpArr)):
        if tmpArr[i] != i:
            return i

    return len(arr)

inputArr = [3, 1, -1, 3]
print findMissingInteger(inputArr)
