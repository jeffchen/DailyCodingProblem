'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
  
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
def productOfAllItem(arr):
    productArr = [1] * len(arr)
    leftArr = [1] * len(arr)
    rightArr = [1] * len(arr)
    # [1, 2, 6, 24]
    for i in xrange(1, len(arr)):
        leftArr[i] = leftArr[i - 1] * arr[i - 1]
        print i, leftArr[i]
    # [120, 60, 20, 5]
    for j in xrange(len(arr) - 2, -1, -1):
        rightArr[j] = rightArr[j + 1] * arr[j + 1]
        print j, rightArr[j]
        
    for x in xrange(len(arr)):
        productArr[x] = leftArr[x] * rightArr[x]

    return productArr


inputArr = [1, 2, 3, 4, 5]
print productOfAllItem(inputArr)
