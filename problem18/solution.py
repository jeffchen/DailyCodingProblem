'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
'''
def findMaxOfSubarray(arr, k):
    res = []
    tmp = []
    # find first round biggest and keep to left: [10, 5, 2]
    for i in xrange(k):
        while res and arr[i] >= arr[res[-1]]:
            res.pop()
        res.append(i)

    for x in xrange(k, len(arr)):
        tmp.append(arr[res[0]])
        # remove index(x - k) elements, these elements are not in k length
        while res and res[0] <= x - k:
            res.pop(0)
        # pop all elements < new element
        while res and arr[x] >= arr[res[-1]]:
            res.pop()

        res.append(x)

    tmp.append(arr[res[0]])
    return tmp


inputArr = [10, 5, 2, 7, 8, 7]
k = 3
print findMaxOfSubarray(inputArr, k)
