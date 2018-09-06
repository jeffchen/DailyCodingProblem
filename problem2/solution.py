'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
def productOfAllItem(arr):
    product = 1

    # product all elements
    for i in arr:
        product = product * i

    # divid each element
    productArr = [None] * len(arr)
    for i in xrange(len(arr)):
        productArr[i] = product / arr[i]

    return productArr

inputArr = [1, 2, 3, 4, 5]
print productOfAllItem(inputArr)
