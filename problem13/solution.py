'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''
def longestKSubstring(string, k):
    window = string[0]
    diffCount = 1
    leftIndex = 0
    maxLeftIndex = 0
    maxRightIndex = 0

    for rightIndex in xrange(1, len(string)):
        if string[rightIndex] not in string[leftIndex:rightIndex]:
            diffCount = diffCount + 1
            if diffCount > k:
                leftIndex = leftIndex + string[leftIndex:rightIndex].rfind(string[leftIndex]) + 1
                diffCount = diffCount - 1

        if rightIndex - leftIndex >= maxRightIndex - maxLeftIndex:
            maxLeftIndex = leftIndex
            maxRightIndex = rightIndex
    
    return string[maxLeftIndex:maxRightIndex + 1]

inputStr = "abcba"
print longestKSubstring(inputStr, 2)
