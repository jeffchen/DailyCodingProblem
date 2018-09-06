'''
Good morning! Here's your coding interview problem for today.
  
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
def sumOfTwoNumber(arr, k):
    # sort first -> [3, 7, 10, 15]
    arr.sort()

    i = 0
    j = len(arr) - 1

    # first round: 3 + 15 = 18 > 17, so move right index
    # second round: 3 + 10 = 13 < 17, so move left index
    # third round: 7 + 10 = 17 == 17, got it
    while i != j:
        if arr[i] + arr[j] > k:
            j = j - 1
        elif arr[i] + arr[j] < k:
            i = i + 1
        else:
            return True

    return False

inputArr = [10, 15, 3, 7]
inputK = 17

print sumOfTwoNumber(inputArr, inputK)
